from image_generation_utils import *
from image_mod_gen_utils import *
from analysis_nn import *
from update_library import *

lib = update_library()

def gen_image(sample):
    fg = []
    for s in range(len(sample[1])):
        fg += [fg_obj(fg_id=sample[1][s], x=sample[2][s], y=sample[3][s])]
    return gen_comp_img(lib, fg, bg_id=sample[0][0], brightness=sample[4][0], sharpness=sample[5][0], contrast=sample[5][0], color=sample[5][0])

def scale_sample(sample, sampling_domain):
    '''Scale a [0,1] sample in a given domain'''
    for i in range(len(sample)):
        sample[i] = sample[i]*(sampling_domain[i][1] - sampling_domain[i][0]) + sampling_domain[i][0]
    return sample



def random_sample(typ, domain, n_samples):

    sample = []
    for _ in range(n_samples):
        if typ == 'float':
            r = random.random()*(domain[1]-domain[0])+domain[0]
        elif typ == 'int':
            r = random.choice(range(domain[0],domain[1]))
        else:
            print('Error')
        sample.append(r)
    return sample

def random_config(domains, n_cars):
#     print("domains is : ", domains)# [[52, 72], [1, 19], [0, 1], [0.35, 1], [0.8, 1.2], [0.7, 1]]
#     print("n_cars is : ", n_cars)
    # Scene and cars
    sample = [random_sample('int',domains[0],1)]
    sample += [random_sample('int',domains[1],n_cars)]
    # Modifications
    x_sample = []
    y_sample = []
    if n_cars > 0:
        step_x = float(domains[2][1])/n_cars
        step_y = float(domains[3][1])/n_cars

        base_x = 0
        base_y = 0
        for _ in range(n_cars):
            x_sample.append(random.uniform(base_x, base_x+step_x))
            y_sample.append(random.uniform(base_y, base_y+step_y))
            base_x += step_x
            base_y += step_y

    shuffle(x_sample)
    y_sample.sort(reverse=True)
    sample += [x_sample]
    sample += [y_sample]

    sample += [random_sample('float',domains[4],1)]
    sample += [random_sample('float',domains[5],1)]

    return sample


def box_2_kitti_format(box):
    '''Transform box for KITTI label format'''
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    left = int(x - w/2)
    right = int(x + w/2)
    top = int(y - h/2)
    bot = int(y + h/2)
    return [left,top,right,bot]

def get_area_cap((x1_c, y1_c, l1, w1), (x2_c, y2_c, l2, w2)):
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

    return max(area_cap,0)


def iou((x1_c, y1_c, l1, w1), (x2_c, y2_c, l2, w2)):

    area_1 = l1*w1
    area_2 = l2*w2

    area_cap = get_area_cap((x1_c, y1_c, l1, w1), (x2_c, y2_c, l2, w2))

    return area_cap/float(area_1+area_2-area_cap)


def iomin((x1_c, y1_c, l1, w1), (x2_c, y2_c, l2, w2)):
    area_1 = l1*w1
    area_2 = l2*w2
    area_cap = get_area_cap((x1_c, y1_c, l1, w1), (x2_c, y2_c, l2, w2))

    min_area = min(area_1, area_2)

    return area_cap / float(min_area)

def save_image(img, file_name, path_data_set):
    '''Save image and label'''

    img_file_name = path_data_set + 'images/' + file_name + '.png'
    img.save(img_file_name)


def save_label(ground_boxes, file_name, path_data_set):
    '''Save label'''

    f = open(path_data_set + 'labels/' + file_name + '.txt', 'w')

    if len(ground_boxes) > 0:
        for box in ground_boxes[:-1]:
            label = [0,0,0] + box_2_kitti_format(box) + [0,0,0,0,0,0,0]
            label = list(map(str, label))
            label = " ".join(label)
            label  = "Car " + label + "\n"
            f.write(label)  # python will convert \n to os.linesep
        label = [0,0,0] + box_2_kitti_format(ground_boxes[-1]) + [0,0,0,0,0,0,0]
        label = list(map(str, label))
        label = " ".join(label)
        label  = "Car " + label
        f.write(label)  # python will convert \n to os.linesep
    f.close()


def pad_sample(conf):
    '''Covert config to list'''
    MAX_NUM_CARS = 3
    pad = MAX_NUM_CARS - len(conf[1])

    pt = conf[0]                # background
    pt += (conf[1] + [-1]*pad)  # car models
    pt += (conf[2] + [-1]*pad)  # x
    pt += (conf[3] + [-1]*pad)  # y
    pt += conf[4]               # image params
    pt += conf[5]
    pt += conf[6]
    pt += conf[7]

    return pt
