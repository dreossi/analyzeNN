from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cv2
import time
import sys
import os
import glob

import numpy as np
import tensorflow as tf


# TOM: hack to import from submodule without __init.py__ (can we fix it?)
import sys
#ROOT_PATH = '/home/tommaso/interact/squeezeDet/'
ROOT_PATH = './squeezeDet/'
sys.path.insert(0, ROOT_PATH + 'src')

from config import *
from train import _draw_box
from nets import *

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('mode', 'image', """'image' or 'video'.""")
#tf.app.flags.DEFINE_string('checkpoint', ROOT_PATH + 'data/model_checkpoints/squeezeDet/model.ckpt-87000',"""Path to the model parameter file.""")
tf.app.flags.DEFINE_string('checkpoint', ROOT_PATH + 'data/model_checkpoints/squeezeTest/model.ckpt-1000',"""Path to the model parameter file.""")

def init():

  with tf.Graph().as_default():

    # Load model
    mc = kitti_squeezeDet_config()
    mc.BATCH_SIZE = 1
    # model parameters will be restored from checkpoint
    mc.LOAD_PRETRAINED_MODEL = False
    model = SqueezeDet(mc, FLAGS.gpu)

    # Start tensorflow session
    saver = tf.train.Saver(model.model_params)
    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
    saver.restore(sess, FLAGS.checkpoint)

    return (sess,mc,model)



def classify(im_path,conf):

    (sess,mc,model) = conf;
    im = cv2.imread(im_path)
    im = im.astype(np.float32, copy=False)
    im = cv2.resize(im, (mc.IMAGE_WIDTH, mc.IMAGE_HEIGHT))
    input_image = im - mc.BGR_MEANS

    # Detect
    det_boxes, det_probs, det_class = sess.run(
     [model.det_boxes, model.det_probs, model.det_class],
     feed_dict={model.image_input:[input_image], model.keep_prob: 1.0})

    # Filter
    final_boxes, final_probs, final_class = model.filter_prediction(
     det_boxes[0], det_probs[0], det_class[0])

    #keep_idx    = [idx for idx in range(len(final_probs)) \
    #                   if final_probs[idx] > mc.PLOT_PROB_THRESH]

    keep_idx = [idx for idx in range(len(final_probs)) \
                if final_probs[idx] > 0.1]

    final_boxes = [final_boxes[idx] for idx in keep_idx]
    final_probs = [final_probs[idx] for idx in keep_idx]
    final_class = [final_class[idx] for idx in keep_idx]

    # # Extract labels + confidence values
    # res = []
    # for label, confidence, box in zip(final_class, final_probs, final_boxes):
    #     res.append((label,confidence,box))
    # return res

    cls2clr = {
        'car': (255, 191, 0),
        'cyclist': (0, 191, 255),
        'pedestrian':(255, 0, 191)
    }
    # Draw boxes
    _draw_box(
        im, final_boxes,
        [mc.CLASS_NAMES[idx]+': (%.2f)'% prob \
            for idx, prob in zip(final_class, final_probs)],
        cdict=cls2clr,
    )

    out_file_name = os.path.join('./', 'tmp.png')
    cv2.imwrite(out_file_name, im)
    #print ('Image detection output saved to {}'.format(out_file_name))

    return (final_boxes,final_probs,final_class)


# Compute intersection over union of b1 = (x1_c, y1_c, l1, w1) and b2 = (x2_c, y2_c, l2, w2)
def iou((x1_c, y1_c, l1, w1), (x2_c, y2_c, l2, w2)):
    left_1 = x1_c - (l1/2)
    right_1 = x1_c + (l1/2)
    top_1 = y1_c - (w1/2)
    bot_1 = y1_c + (w1/2)
    left_2 = x2_c - (l2/2)
    right_2 = x2_c + (l2/2)
    top_2 = y2_c - (w2/2)
    bot_2 = y2_c + (w2/2)

    left_cap = max(left_1, left_2)
    right_cap = min(right_1, right_2)
    top_cap = max(top_1, top_2)
    bot_cap = min(bot_1, bot_2)

    area_1 = l1*w1
    area_2 = l2*w2
    area_cap = (right_cap-left_cap)*(bot_cap-top_cap)

    return area_cap/(area_1+area_2-area_cap)
