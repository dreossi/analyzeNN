from gen_utils import *
import squeezedet as nn

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

PREFIX_LABELS = '/home/tommaso/squeezeDet/data/KITTI/training/label_2/'
PREFIX_IMAGES = '/home/tommaso/squeezeDet/data/KITTI/training/image_2/'
CHECKPOINT_DIR = '/home/tommaso/analyzeNN/data/train_0/checkpoint/train/'

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
        (boxes, probs, _)= nn.classify(PREFIX_IMAGES + i + '.png', net)
        thresh_boxes = []
        for box, prob in zip(boxes, probs):
            if prob > 0.5:
                thresh_boxes += [box]
        predictions[i] = thresh_boxes

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
    plt.plot(x, y2, 'r', x, y1, 'g')
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
        ap, rec = average_precision(gt, pred, 0.5)
        tot_ap += ap
        tot_rec += rec
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

checkpoint_list = range(0,5000,200)
image_set = '/home/tommaso/squeezeDet/data/KITTI/ImageSets/test_mix.txt'

res = eval_train(checkpoint_list, image_set)
plot_results(res)
