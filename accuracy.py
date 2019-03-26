from gen_utils import *
import squeezedet as nn

def edge_2_cent(box):
    xl = box[0]
    yt = box[1]
    xr = box[2]
    yb = box[3]
    w = xr-xl
    h = yb-yt
    xc = xl + w/2
    yc = yt + h/2
    return (xc,yc,w,h)

def pred_2_detect(preds, gt, iou_tresh):
    '''Assign predictions to detections'''
    detetctions = []
    for p in preds:
        detects = []
        for g in gt:
            detects += [iou(p, g) > iou_tresh]
        detetctions += [detects]
    print(detetctions)
    assigns = []
    for d in detetctions:
        a = -1
        for i in range(len(d)):
            if d[i]:
                a = i
        assigns += [a]

    assigns = duplicate_false_positive(assigns, len(gt))
    return assigns

def duplicate_false_positive(detects, n_gt):
    '''Correct double false positives'''
    for i in range(n_gt):
        first_occ = True
        for j in range(len(detects)):
            if i == detects[j]:
                if first_occ:
                    first_occ = False
                else:
                    detects[j] = -1
    return detects


def prec_rec(detects, n_gt):
    '''Compute precision and recall'''

    tp = sum(d != -1 for d in detects)
    fp = sum(d == -1 for d in detects)
    fn = sum(g not in detects for g in range(n_gt))

    print((tp, fp, fn))

    prec = tp/float(tp+fp)
    rec = tp/float(tp+fn)

    return prec, rec


def precision_recall(preds, gt_boxes, iou_tresh):
    detects = pred_2_detect(preds, gt_boxes, iou_tresh)
    return prec_rec(detects, len(gt_boxes))




checkpoint = '/home/tommaso/analyzeNN/data/train_0/checkpoint/train/model.ckpt-5000'
net = nn.init(checkpoint)

tmp_img_file_name = "/home/tommaso/analyzeNN/data/test/images/h_m_0_3_000006.png"

gt_b_1 = edge_2_cent([641, 181, 675, 209])
gt_b_2 = edge_2_cent([598, 178, 644, 214])
gt_b_3 = edge_2_cent([514, 162, 604, 236])



gt_boxes = [gt_b_1, gt_b_2, gt_b_3]
(boxes,probs,cats) = nn.classify(tmp_img_file_name,net)
