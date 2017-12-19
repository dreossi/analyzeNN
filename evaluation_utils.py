from gen_utils import *
import squeezedet as nn

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import pickle

CHECKPOINT_DIR = './data/train_3/checkpoint/train/'

PREFIX_LABELS = './data/train_0/mis/labels/'
PREFIX_IMAGES = './data/train_0/mis/images/'
image_set = './data/train_0/mis/test_mis.txt'

# PREFIX_LABELS = './data/train_0/train/mix/labels/'
# PREFIX_IMAGES = './data/train_0/train/mix/images/'
# image_set = './data/train_0/train/mix/image_sets/test.txt'

IOU_THRESH = 0.5
NN_PROB_THRESH = 0.5

def read_label(file_name):
    '''Read label from file (KITTI format)'''
    with open(file_name, "r") as f:
        content = f.readlines()
    content = [c.strip().split(" ") for c in content]
    labels = []
    for c in content:
        labels += [[float(c[4]), float(c[5]), float(c[6]), float(c[7])]]

    return labels

def read_image_set(image_set):
    '''Read image names from image set'''
    with open(image_set, "r") as f:
        content = f.readlines()
    images = [c.strip() for c in content]

    gt_labels = dict()
    for i in images:
        labels = read_label(PREFIX_LABELS + i + '.txt')
        label_boxes = [ kitti_2_box_format(l) for l in labels ]
        gt_labels[i] = label_boxes
    return gt_labels


def predict(net, image_set):
    '''Run neural net on images from image_set'''

    with open(image_set, "r") as f:
        content = f.readlines()
    images = [c.strip() for c in content]

    predictions = dict()
    for i in images:
        (boxes, probs, _) = nn.classify(PREFIX_IMAGES + i + '.png', net, NN_PROB_THRESH)
        predictions[i] = boxes

    return predictions


def average_precision(gt, prediction, iou_thresh):
    '''Average precision of prediction'''
    alread_detected = [False]*len(gt)
    tp = 0
    fp = 0
    fn = 0

    if not(prediction):
        return 0, 0

    for pred in prediction:
        detect = False
        for i in range(len(gt)):
            #print(iou(pred, gt[i]))
            if iou(pred, gt[i]) > iou_thresh:
                detect = True
                if not alread_detected[i]:
                    tp += 1
                    alread_detected[i] = True
                else:
                    fp += 1
        if not detect:
            fp += 1
    fn = alread_detected.count(False)
    ap = tp/float(tp+fp)
    recall = tp/float(tp+fn)
    return ap, recall


def plot_boxes(image, gt, pred):
    '''Plot gt and prediction boxes'''
    im = np.array(Image.open(PREFIX_IMAGES + image + '.png'), dtype=np.uint8)
    fig,ax = plt.subplots(1)
    ax.imshow(im)
    for box in gt:
        rect = patches.Rectangle((box[0]-box[2]/2, box[1]-box[3]/2),box[2],box[3],linewidth=1,edgecolor='b',facecolor='none')
        ax.add_patch(rect)
    for box in pred:
        rect = patches.Rectangle((box[0]-box[2]/2, box[1]-box[3]/2),box[2],box[3],linewidth=1,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
    plt.show()

def plot_results(results):
    '''Plot results'''
    cps = []
    aps = []
    recs = []
    for cp in results:
        (ap,rec) = results[cp]
        cps += [cp]
        aps += [ap]
        recs += [rec]
    order = np.argsort(cps)
    x = np.array(cps)[order]
    y1 = np.array(aps)[order]
    y2 = np.array(recs)[order]
    plt.plot(x, y2, 'r', x, y1, 'b')
    plt.show()



def eval_set(net, image_set):
    '''Evaluate net on image_set'''

    gt_labels = read_image_set(image_set)
    predictions = predict(net, image_set)

    tot_ap = 0
    tot_rec = 0
    for image in gt_labels:
        gt = gt_labels[image]
        pred = predictions[image]
        ap, rec = average_precision(gt, pred, IOU_THRESH)
        tot_ap += ap
        tot_rec += rec
        print(image + ': ' + str(ap) + ', ' + str(rec) )
        #print(gt)
        #print(pred)
        #plot_boxes(image, gt,pred)

    tot_ap = tot_ap/float(len(gt_labels))
    tot_rec = tot_rec/float(len(gt_labels))

    return tot_ap, tot_rec


def eval_train(checkpoint_list, image_set):
    '''Evaluate training on list of stored checkpoints'''
    results = dict()
    for cp in checkpoint_list:
        cp_path = CHECKPOINT_DIR + 'model.ckpt-' + str(cp)
        print('Evaluating: ' + cp_path)
        net = nn.init(cp_path)
        ap, recall = eval_set(net, image_set)
        results[cp] = (ap,recall)
    return results

# checkpoint_list = range(0,5250,250)
#
# res = eval_train(checkpoint_list, image_set)
# pickle.dump( res, open( "save_mis_3.p", "wb" ) )
#
# plot_results(res)
#
#
#
# # cp_path = CHECKPOINT_DIR + 'model.ckpt-5000'
# # net = nn.init(cp_path)
# # eval_set(net, image_set)
