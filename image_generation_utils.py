'''
This file contains helper tools
'''

from collections import namedtuple
import numpy as np
import cv2

bb = namedtuple('bb', ['lr', 'tr', 'tl', 'll'])
scale = namedtuple('scale', ['front', 'back'])
fg_obj = namedtuple('fg_obj', 'x y fg_id')

unit_box = bb([1, 0], [1, 1], [0, 1], [0, 0])

bb_to_array = lambda bbox: np.array([r for r in bbox])

# Tranform 2d box-sample into trapezoid (car displacement area)
def unit_to_bb_h(bounding_box, ld_box=unit_box):

    bbox = bb_to_array(bounding_box)
    ubox = bb_to_array(ld_box)
    h, _ = cv2.findHomography(np.float_(ubox), np.float_(np.array(bbox)))

    return h

def ld_to_bb_sample(sample, h):
    sample = np.float32([sample]).reshape(-1, 1, 2)
    con = cv2.perspectiveTransform(sample, h)
    return np.array(list(con[0][0]))

