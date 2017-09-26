'''
Populate the library with the images and information from what was collected
using the new implementation
'''

import pickle
import numpy as np
from cnn_image_generation.lib_obj import *

BACK_ORIENT = -np.pi/2
FRONT_ORIENT = np.pi/2

road_images= [{'path':'./pics/roads/desert.jpg', \
               'type':'Desert Road'},
              {'path':'./pics/roads/countryside.jpg', \
               'type':'Countryside Road'},
              {'path':'./pics/roads/city.jpg', \
               'type': 'City Road'},
              {'path':'./pics/roads/cropped_desert.jpg', \
               'type':' Cropped Desert Road'}]
for i in range(134, 182):
    road_images.append({'path':'./pics/roads/forest/0000000'\
                               + str(i) + '.png', \
                        'type':'Forest Road'})


road_images.append({'path':'./pics/roads/desert_kitti.png', \
               'type':'Desert Road', 'id':52, 'background_color': 'brown light, blue light', 'environment': 'desert'})
road_images.append({'path':'./pics/roads/city_kitti.png',\
               'type':'City Road', 'id':53, 'background_color': 'brown light, gray', 'environment': 'city'})
road_images.append({'path':'./pics/roads/forest_kitti.png',\
               'type':'Forest Road', 'id':54, 'background_color': 'green light, green dark', 'environment': 'forest'})
road_images.append({'path':'./pics/roads/big_sur_kitti.png',\
               'type':'Big Sur Road', 'id':55, 'background_color': 'brown, blue', 'environment': 'city'})
road_images.append({'path':'./pics/roads/mountain_kitti.jpg',\
               'type':'Mountain Road', 'id':56, 'background_color': 'green', 'environment': 'forest'})
road_images.append({'path':'./pics/roads/bridge_kitti.jpg',\
               'type':'Bridge Road', 'id':57, 'background_color': 'green, red', 'environment': 'forest'})
road_images.append({'path':'./pics/roads/tunnel_kitti.jpg',\
               'type':'Tunnel Road', 'id':58, 'background_color': 'gray', 'environment': 'mountain'})
road_images.append({'path':'./pics/roads/island_kitti.jpg',\
               'type':'Island Road', 'id':59, 'background_color': 'blue light, green, brown light', 'environment': 'field'})
road_images.append({'path':'./pics/roads/countryside_kitti.jpg',\
               'type':'CountrysideRoad', 'id':60, 'background_color': 'green', 'environment': 'forest'})
road_images.append({'path':'./pics/roads/hill_kitti.jpg',\
               'type':'Hill Road', 'id':61, 'background_color': 'green, white', 'environment': 'field'})
road_images.append({'path':'./pics/roads/alps_kitti.png',\
               'type':'Alps Road', 'id':62, 'background_color': 'brown light, gray', 'environment': 'mountain'})
road_images.append({'path':'./pics/roads/bridge_1_kitti.png',\
               'type':'Brisdge 1 Road', 'id':63, 'background_color': 'gray light, blue light', 'environment': 'city'})
road_images.append({'path':'./pics/roads/building_kitti.png',\
               'type':'Building Road', 'id':64, 'background_color': 'gray, brown light', 'environment': 'city'})
road_images.append({'path':'./pics/roads/cloud_kitti.png',\
               'type':'Cloud Road', 'id':65, 'background_color': 'green, brown, black', 'environment': 'field'})
road_images.append({'path':'./pics/roads/downtown_kitti.png',\
               'type':'Downtown Road', 'id':66, 'background_color': 'brown light, yellow, gray', 'environment': 'city'})
road_images.append({'path':'./pics/roads/freeway_kitti.png',\
               'type':'Freeway Road', 'id':67, 'background_color': 'gray', 'environment': 'city'})
road_images.append({'path':'./pics/roads/track_kitti.jpg',\
               'type':'Track Road', 'id':68, 'background_color': 'blue, blue light', 'environment': 'city'})
road_images.append({'path':'./pics/roads/rainforest_kitti.png',\
               'type':'Rainforest Road', 'id':69, 'background_color': 'green, brown light', 'environment': 'forest'})
road_images.append({'path':'./pics/roads/tree_kitti.png',\
               'type':'Tree Road', 'id':70, 'background_color': 'green, yellow', 'environment': 'forest'})
road_images.append({'path':'./pics/roads/trees_kitti.png',\
               'type':'Trees Road', 'id':71, 'background_color': 'green', 'environment': 'forest'})

car_images = [{'path':'./pics/cars/bmw_kitti.png', 'type':'BMW Kitti', \
               'id':0, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/suzuki_kitti.png','type':'Suzuki Kitti',\
                'id':1, 'car_category': 'jeep', 'car_color': 'red dark', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/tesla_kitti.png', 'type':'Tesla Kitti', \
               'id':2, 'car_category': 'car', 'car_color': 'blue dark', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/fiat_kitti.png', 'type':'Fiat Kitti',\
               'id':3, 'car_category': 'car', 'car_color': 'green', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/honda_kitti.png', 'type':'Honda Kitti',\
               'id':4, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/toyota_kitti.png', 'type':'Toyota Kitti',\
               'id':5, 'car_category': 'car', 'car_color': 'white', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/peugeot_kitti.png', 'type':'Peugeot Kitti',\
               'id':6, 'car_category': 'car', 'car_color': 'orange', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/chrysler_kitti.png', 'type':'Chrysler Kitti', \
               'id':7, 'car_category': 'van', 'car_color': 'gray', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/bmw_blue_kitti.png', 'type': 'BMW Blue Kitti', \
               'id':8, 'car_category': 'car', 'car_color': 'blue', 'car_orientation': BACK_ORIENT},
              {'path':'./pics/cars/honda_civic_front_kitti.png', 'type':'Honda Civic Front Kitti', \
               'id':9, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/toyota_camry_front_kitti.png', 'type': 'Toyota Camry Front Kitti', \
               'id':10, 'car_category': 'car', 'car_color': 'cream', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/toyota_prius_front_kitti.png', 'type': 'Toyota Prius Front Kitti', \
               'id':11,  'car_category': 'car', 'car_color': 'white', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/benz_front_kitti.png', 'type': 'Benz Front Kitti', \
               'id':12,  'car_category': 'car', 'car_color': 'white', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/ford_front_kitti.png', 'type': 'Ford Front Kitti', \
               'id':13,  'car_category': 'car', 'car_color': 'red', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/jeep_front_kitti.png', 'type': 'Jeep Front Kitti', \
               'id':14, 'car_category': 'jeep', 'car_color': 'red', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/jeep_cherokee_front_kitti.png', 'type': 'Jeep Cherokee Front Kitti', \
               'id':15, 'car_category': 'jeep', 'car_color': 'cream', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/fiat_front_kitti.png', 'type': 'Fiat Front Kitti', \
               'id':16, 'car_category': 'car', 'car_color': 'yellow', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/bmw_front_kitti.png', 'type': 'BMW Front Kitti', \
               'id':17, 'car_category': 'car', 'car_color': 'blue dark', 'car_orientation': FRONT_ORIENT },
              {'path': './pics/cars/suzuki_front_kitti.png', 'type': 'Suzuki Front Kitti', \
               'id':18, 'car_category': 'jeep', 'car_color': 'red dark', 'car_orientation': FRONT_ORIENT }
              ]

configs_file = 'scene_configs_py2'

convert_sample_to_int = lambda sample, num_elems:  int(sample*(num_elems+1))


def update_library():
    Library = lib_object()
    with open(configs_file, 'rb') as f:
        configs = pickle.load(f)


    for i in range(len(road_images)):
        elem = configs[i]
        im_data = Image.open(road_images[i]['path'])
        if elem != []:
            trapezoid = elem[0]
            scaling = elem[1]
            create_bound = bb(trapezoid[0], trapezoid[1], trapezoid[2], \
                              trapezoid[3])
            create_scale = scale(scaling[0], scaling[1])
            Library.add_backgrounds(im_data=im_data, add_details=road_images[i], \
                                    bounding_boxes=create_bound, \
                                    scale=create_scale)
        else:
            Library.add_backgrounds(im_data=im_data, add_details=road_images[i])



    for car in car_images:
        im_data=Image.open(car['path'])
        Library.add_foregrounds(im_data=im_data,add_details=car)

    return Library


