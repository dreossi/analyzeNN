'''
Populate the library with the images and information from what was collected
using the new implementation
'''

import pickle
from cnn_image_generation.lib_obj import *

road_images= [{'path':'./pics/roads/desert_kitti.png', \
               'type':'Desert Road', 'id':52},
              {'path':'./pics/roads/city_kitti.png',\
               'type':'City Road', 'id':53},
              {'path':'./pics/roads/forest_kitti.png',\
               'type':'Forest Road', 'id':54},
              {'path':'./pics/roads/big_sur_kitti.png',\
               'type':'Big Sur Road', 'id':55},
              {'path':'./pics/roads/mountain_kitti.jpg',\
               'type':'Mountain Road', 'id':56},
              {'path':'./pics/roads/bridge_kitti.jpg',\
               'type':'Bridge Road', 'id':57},
              {'path':'./pics/roads/tunnel_kitti.jpg',\
               'type':'Tunnel Road', 'id':58},
              {'path':'./pics/roads/island_kitti.jpg',\
               'type':'Island Road', 'id':59},
              {'path':'./pics/roads/countryside_kitti.jpg',\
               'type':'CountrysideRoad', 'id':60},
              {'path':'./pics/roads/hill_kitti.jpg',\
               'type':'Hill Road', 'id':61},
              {'path':'./pics/roads/alps_kitti.png',\
               'type':'Alps Road', 'id':62},
              {'path':'./pics/roads/bridge_1_kitti.png',\
               'type':'Brisdge 1 Road', 'id':63},
              {'path':'./pics/roads/building_kitti.png',\
               'type':'Building Road', 'id':64},
              {'path':'./pics/roads/cloud_kitti.png',\
               'type':'Cloud Road', 'id':65},
              {'path':'./pics/roads/downtown_kitti.png',\
               'type':'Downtown Road', 'id':66},
              {'path':'./pics/roads/freeway_kitti.png',\
               'type':'Freeway Road', 'id':67},
              {'path':'./pics/roads/track_kitti.jpg',\
               'type':'Track Road', 'id':68},
              {'path':'./pics/roads/rainforest_kitti.png',\
               'type':'Rainforest Road', 'id':69},
              {'path':'./pics/roads/tree_kitti.png',\
               'type':'Tree Road', 'id':70},
              {'path':'./pics/roads/trees_kitti.png',\
               'type':'Trees Road', 'id':71}]

car_images = [{'path':'./pics/cars/bmw_kitti.png', 'type':'BMW Kitti', \
               'id':0},
              {'path':'./pics/cars/suzuki_kitti.png','type':'Suzuki Kitti',\
                'id':1},
              {'path':'./pics/cars/tesla_kitti.png', 'type':'Tesla Kitti', \
               'id':2},
              {'path':'./pics/cars/fiat_kitti.png', 'type':'Fiat Kitti',\
               'id':3},
              {'path':'./pics/cars/honda_kitti.png', 'type':'Honda Kitti',\
               'id':4},
              {'path':'./pics/cars/toyota_kitti.png', 'type':'Toyota Kitti',\
               'id':5},
              {'path':'./pics/cars/peugeot_kitti.png', 'type':'Peugeot Kitti',\
               'id':6},
              {'path':'./pics/cars/chrysler_kitti.png', \
               'type':'Chrysler Kitti', 'id':7},
              {'path':'./pics/cars/bmw_blue_kitti.png', \
               'type': 'BMW Blue Kitti', 'id':8},
              {'path':'./pics/cars/honda_civic_front_kitti.png', \
               'type':'Honda Civic Front Kitti', 'id':9},
              {'path': './pics/cars/toyota_camry_front_kitti.png', \
               'type': 'Toyota Camry Front Kitti', 'id':10},
              {'path': './pics/cars/toyota_prius_front_kitti.png', \
               'type': 'Toyota Prius Front Kitti', 'id':11},
              {'path': './pics/cars/benz_front_kitti.png', \
               'type': 'Benz Front Kitti', 'id':12},
              {'path': './pics/cars/ford_front_kitti.png',
               'type': 'Ford Front Kitti', 'id':13},
              {'path': './pics/cars/jeep_front_kitti.png', \
               'type': 'Jeep Front Kitti', 'id':14},
              {'path': './pics/cars/jeep_cherokee_front_kitti.png', \
               'type': 'Jeep Cherokee Front Kitti', 'id':15},
              {'path': './pics/cars/fiat_front_kitti.png',
               'type': 'Fiat Front Kitti', 'id':16},
              {'path': './pics/cars/bmw_front_kitti.png', \
               'type': 'BMW Front Kitti', 'id':17},
              {'path': './pics/cars/suzuki_front_kitti.png', \
               'type': 'Suzuki Front Kitti', 'id':18}
              ]

configs_file = 'scene_configs'

convert_sample_to_int = lambda sample, num_elems:  int(sample*(num_elems+1))


def update_library():
    Library = lib_object()
    with open(configs_file, 'rb') as f:
        configs = pickle.load(f)

    i = 0
    for elem in configs:
        if elem != []:
            im_data = Image.open(road_images[i]['path'])
            bounding_box = elem[0]
            scaling = elem[1]
            create_bound = bb(bounding_box[0], bounding_box[1], bounding_box[2], \
                              bounding_box[3])
            create_scale = scale(scaling[0], scaling[1])
            Library.add_backgrounds(im_data=im_data,add_details=road_images[i], \
                                    bounding_boxes = create_bound, \
                                    scale=create_scale)
            i+=1

    for car in car_images:
        im_data=Image.open(car['path'])
        Library.add_foregrounds(im_data=im_data,add_details=car)

    return Library


