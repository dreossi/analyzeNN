from gen_utils import *
import squeezedet as nn

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

import pickle
import random

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

def plot_results(x,ys):
    plt.plot(x, ys)
    plt.show()


def get_ap_rec(res):
    '''Get check points, avg precision, and recall from results'''
    cps = []
    aps = []
    recs = []
    for cp in res:
        (ap,rec) = res[cp]
        cps += [cp]
        aps += [ap]
        recs += [rec]
    order = np.argsort(cps)
    x = np.array(cps)[order]
    y1 = np.array(aps)[order]
    y2 = np.array(recs)[order]
    return x, y1, y2



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
        #print(image + ': ' + str(ap) + ', ' + str(rec) )
        #print(gt)
        #print(pred)
        #plot_boxes(image, gt,pred)

    tot_ap = tot_ap/float(len(gt_labels))
    tot_rec = tot_rec/float(len(gt_labels))

    return tot_ap, tot_rec


def eval_train(checkpoint_dir, checkpoint_list, image_set):
    '''Evaluate training on list of stored checkpoints'''
    results = dict()
    for cp in checkpoint_list:
        cp_path = checkpoint_dir + 'model.ckpt-' + str(cp)
        print('Evaluating: ' + cp_path)
        net = nn.init(cp_path)
        ap, recall = eval_set(net, image_set)
        results[cp] = (ap,recall)
    return results


def gen_augmented_set(image_set, i_start, i_end, n):
    '''Augment images_set with n images with indices are between i_start and i_end'''

    for i in range(1,4):

        PREFIX = 'm_2_' + str(i) + '_'

        arr = range(i_start,i_end)
        random.shuffle(arr)

        arr = arr[0:n]

        with open(image_set, 'a') as f:
            for a in arr:
                f.write(PREFIX + str(a).zfill(6) + '\n')


def multiple_checkpoint_eval():

    checkpoint_list = range(0,5250,250)

    #for i in range(1,4):
    for j in range(1,4):
        #checkpoint_dir = './data/train_' + str(i) + '/' + 'checkpoint_' + str(i) + '_' + str(j) + '/train/'
        checkpoint_dir = './data/train_0/' + 'checkpoint' + '/train/'
        res = eval_train(checkpoint_dir, checkpoint_list, image_set)
        pickle.dump( res, open( "save_mis_05_" + str(j) +".p", "wb" ) )
        #pickle.dump( res, open( "save_mis_"+ str(i) + "_" + str(j) +".p", "wb" ) )


def avg_eval(result_list):
    '''Load results and average them'''
    all_ap = []
    all_rec = []
    for res_l in result_list:
        res = pickle.load( open( res_l, "rb" ) )
        cp, ap, rec = get_ap_rec(res)
        all_ap += [ap]
        all_rec += [rec]
    return cp, np.mean(all_ap,axis=0), np.mean(all_rec,axis=0)



#gen_augmented_set('./data/train_05/train/image_sets/train_05_3.txt', 250, 500, 40)
#
#
#
# res = eval_train(checkpoint_list, image_set)
# pickle.dump( res, open( "save_mis_0.p", "wb" ) )
#
# plot_results(res)
#
#
#
# # cp_path = CHECKPOINT_DIR + 'model.ckpt-5000'
# # net = nn.init(cp_path)
# # eval_set(net, image_set)

#multiple_checkpoint_eval()



checkpoint_list = [500]
#
# aug_round = 2
# ratios = ['08','17','35','50']
# test = 0
#


dirs = 'mis_0', 'mis_halt', 'class_aug', 'mis_dist', 'mis_mix'
sets = 'test_mis.txt', 'test_halt.txt', 'test_aug.txt', 'test_mis.txt', 'test_mix.txt'

test = 3

PREFIX = '/home/tommaso/squeezeDet/data/webots/test/'
PREFIX_LABELS = PREFIX + 'labels/'
PREFIX_IMAGES = PREFIX + 'images/'
image_set = 'test.txt'
#
# PREFIX = './data/train_0/train'
# PREFIX_LABELS = PREFIX + '/labels/'
# PREFIX_IMAGES = PREFIX + '/images/'
# image_set = PREFIX + '/image_sets/test.txt'
#
#
# for ratio in ratios:
#     res = eval_train('./data/train_' + str(aug_round) + '_' + str(ratio) + '/checkpoint/train/', checkpoint_list, image_set)
#     file_name = 'save_' + str(aug_round) + '_' + str(ratio) + '_' + str(test) + '.p'
#     pickle.dump( res, open( file_name, "wb" ) )
#     _, ap, rec = avg_eval([file_name])
#     print(ratio)
#     print('ap: ' + str(np.max(ap)))
#     print('rec: ' + str(np.max(rec)))

# ratio = 0
res = eval_train('/home/tommaso/squeezeDet/data/webots/train/checkpoints', checkpoint_list, image_set)

file_name = 'save_0_test_err.p'
pickle.dump( res, open( file_name, "wb" ) )
_, ap, rec = avg_eval([file_name])
#print(ratio)
print('ap: ' + str(np.max(ap)))
print('rec: ' + str(np.max(rec)))
#
#

# cp, ap, rec = avg_eval(['./data/train_05/save_mis_05_1.p'])
# #plot_results(cp,ap)
# print(ap)
# print(rec)
#
# for test in tests:
#     PRE = './data/train_' + str(test) + '/save_mis_' + str(test) + '_'
#     aps = []
#     recs = []
#     for i in range(1,4,1):
#         exp = PRE + str(i) + '.p'
#         _, ap, rec = avg_eval([exp])
#         aps += [np.max(ap)]
#         recs += [np.max(rec)]
#     print(PRE)
#     print(np.mean(aps))
#     print(np.mean(recs))


# checkpoint_list = range(4500,5250,250)
# #
# # aug_round = 2
# # ratios = ['08','17','35','50']
# # test = 0
# #
# PREFIX = './data/mis_dist'
# PREFIX_LABELS = PREFIX + '/labels/'
# PREFIX_IMAGES = PREFIX + '/images/'
# image_set = PREFIX + '/test_mis.txt'
# #
# #
#
# res = eval_train('/home/tommaso/analyzeNN/data/train_dist/checkpoint_dist/train/', checkpoint_list, image_set)
# file_name = 'save_dist.p'
# pickle.dump( res, open( file_name, "wb" ) )
# _, ap, rec = avg_eval([file_name])
# print('ap: ' + str(np.max(ap)))
# print('rec: ' + str(np.max(rec)))
