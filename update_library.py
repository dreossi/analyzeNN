'''
Populate the library with the images and information from what was collected
using the new implementation
'''

import pickle
import numpy as np
from lib_obj import *

BACK_ORIENT = -np.pi/2
FRONT_ORIENT = np.pi/2

road_images= [{'road_path':'./pics/roads/desert.jpg', \
               'road_type':'Desert Road'},
              {'road_path':'./pics/roads/countryside.jpg', \
               'road_type':'Countryside Road'},
              {'road_path':'./pics/roads/city.jpg', \
               'road_type': 'City Road'},
              {'road_path':'./pics/roads/cropped_desert.jpg', \
               'road_type':' Cropped Desert Road'}]
for i in range(134, 182):
    road_images.append({'road_path':'./pics/roads/forest/0000000'\
                               + str(i) + '.png', \
                        'road_type':'Forest Road'})


road_images.append({'road_path':'./pics/roads/desert_kitti.png', \
               'road_type':'Desert Road', 'road_id':52, 'background_color': 'brown light, blue light', 'environment': 'desert'})
road_images.append({'road_path':'./pics/roads/city_kitti.png',\
               'road_type':'City Road', 'road_id':53, 'background_color': 'brown light, gray', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/forest_kitti.png',\
               'road_type':'Forest Road', 'road_id':54, 'background_color': 'green light, green dark', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/big_sur_kitti.png',\
               'road_type':'Big Sur Road', 'road_id':55, 'background_color': 'brown, blue', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/mountain_kitti.jpg',\
               'road_type':'Mountain Road', 'road_id':56, 'background_color': 'green', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/bridge_kitti.jpg',\
               'road_type':'Bridge Road', 'road_id':57, 'background_color': 'green, red', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/tunnel_kitti.jpg',\
               'road_type':'Tunnel Road', 'road_id':58, 'background_color': 'gray', 'environment': 'mountain'})
road_images.append({'road_path':'./pics/roads/island_kitti.jpg',\
               'road_type':'Island Road', 'road_id':59, 'background_color': 'blue light, green, brown light', 'environment': 'field'})
road_images.append({'road_path':'./pics/roads/countryside_kitti.jpg',\
               'road_type':'Countryside Road', 'road_id':60, 'background_color': 'green', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/hill_kitti.jpg',\
               'road_type':'Hill Road', 'road_id':61, 'background_color': 'green, white', 'environment': 'field'})
road_images.append({'road_path':'./pics/roads/alps_kitti.png',\
               'road_type':'Alps Road', 'road_id':62, 'background_color': 'brown light, gray', 'environment': 'mountain'})
road_images.append({'road_path':'./pics/roads/bridge_1_kitti.png',\
               'road_type':'Bridge 1 Road', 'road_id':63, 'background_color': 'gray light, blue light', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/building_kitti.png',\
               'road_type':'Building Road', 'road_id':64, 'background_color': 'gray, brown light', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/cloud_kitti.png',\
               'road_type':'Cloud Road', 'road_id':65, 'background_color': 'green, brown, black', 'environment': 'field'})
road_images.append({'road_path':'./pics/roads/downtown_kitti.png',\
               'road_type':'Downtown Road', 'road_id':66, 'background_color': 'brown light, yellow, gray', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/freeway_kitti.png',\
               'road_type':'Freeway Road', 'road_id':67, 'background_color': 'gray', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/track_kitti.jpg',\
               'road_type':'Track Road', 'road_id':68, 'background_color': 'blue, blue light', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/rainforest_kitti.png',\
               'road_type':'Rainforest Road', 'road_id':69, 'background_color': 'green, brown light', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/tree_kitti.png',\
               'road_type':'Tree Road', 'road_id':70, 'background_color': 'green, yellow', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/trees_kitti.png',\
               'road_type':'Trees Road', 'road_id':71, 'background_color': 'green', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/fields_kitti.png',\
               'road_type':'Fields Road', 'road_id':72, 'background_color': 'green, brown', 'environment': 'forest, fields'})
road_images.append({'road_path':'./pics/roads/construction_kitti.png',\
               'road_type':'Construction Road', 'road_id':73, 'background_color': 'gray, brown', 'environment': 'city'})
road_images.append({'road_path':'./pics/roads/little_bridge_kitti.jpg',\
               'road_type':'Little Bridge', 'road_id':74, 'background_color': 'green, gray', 'environment': 'forest'})
road_images.append({'road_path':'./pics/roads/parking_lot_kitti.png',\
               'road_type':'Parking Lot', 'road_id':75, 'background_color': 'gray', 'environment': 'city, parking'})
road_images.append({'road_path':'./pics/roads/indoor_parking_kitti.png',\
               'road_type':'Indoor Parking Road', 'road_id':76, 'background_color': 'gray', 'environment': 'city, parking'})
road_images.append({'road_path':'./pics/roads/freeway_moto_kitti.jpg',\
               'road_type':'Freeway Moto Road', 'road_id':77, 'background_color': 'black, brow', 'environment': 'desert, freeway'})
road_images.append({'road_path':'./pics/roads/freeway_kitti.jpg',\
               'road_type':'Freeway Road', 'road_id':78, 'background_color': 'black, blue, green', 'environment': 'freeway'})
road_images.append({'road_path':'./pics/roads/snow_kitti.jpg',\
               'road_type':'Snow Road', 'road_id':79, 'background_color': 'white', 'environment': 'snow, forest'})
road_images.append({'road_path':'./pics/roads/icy_kitti.jpg',\
               'road_type':'Icy Road', 'road_id':80, 'background_color': 'white', 'environment': 'snow, forest'})
road_images.append({'road_path':'./pics/roads/night_road_kitti.jpg',\
               'road_type':'Night Road', 'road_id':81, 'background_color': 'black', 'environment': 'fields'})
road_images.append({'road_path':'./pics/roads/night_bridge_kitti.jpg',\
               'road_type':'Night Bridge Road', 'road_id':82, 'background_color': 'black', 'environment': 'bridge'})
road_images.append({'road_path':'./pics/roads/in_tunnel_kitti.jpg',\
               'road_type':'In Tunnel Road', 'road_id':83, 'background_color': 'gray, blue, red', 'environment': 'tunnel'})
road_images.append({'road_path':'./pics/roads/rainy_bridge_kitti.jpg',\
               'road_type':'Rainy Bridge Road', 'road_id':84, 'background_color': 'gray, blue', 'environment': 'bridge'})
road_images.append({'road_path':'./pics/roads/joshua_tree_kitti.jpg',\
               'road_type':'Joshua Tree Road', 'road_id':85, 'background_color': 'brown, green, blue', 'environment': 'desert'})
road_images.append({'road_path':'./pics/roads/yosemite_kitti.png',\
               'road_type':'Yosemite Road', 'road_id':86, 'background_color': 'gray, green, blue', 'environment': 'forest'})


car_images = [{'car_path':'./pics/cars/bmw_gray_front_kitti.png', 'type':'BMW Kitti', \
               'car_id':0, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/suzuki_rear_kitti.png','type':'Suzuki Kitti',\
                'car_id':1, 'car_category': 'jeep', 'car_color': 'red dark', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/tesla_rear_kitti.png', 'type':'Tesla Kitti', \
               'car_id':2, 'car_category': 'car', 'car_color': 'white', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/fiat_front_kitti.png', 'type':'Fiat Kitti',\
               'car_id':3, 'car_category': 'car', 'car_color': 'green', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/honda_kitti.png', 'type':'Honda Kitti',\
               'car_id':4, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/toyota_kitti.png', 'type':'Toyota Kitti',\
               'car_id':5, 'car_category': 'car', 'car_color': 'white', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/peugeot_kitti.png', 'type':'Peugeot Kitti',\
               'car_id':6, 'car_category': 'car', 'car_color': 'orange', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/chrysler_kitti.png', 'type':'Chrysler Kitti', \
               'car_id':7, 'car_category': 'van', 'car_color': 'gray', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/bmw_blue_kitti.png', 'type': 'BMW Blue Kitti', \
               'car_id':8, 'car_category': 'car', 'car_color': 'blue', 'car_orientation': BACK_ORIENT},
              {'car_path':'./pics/cars/honda_civic_front_kitti.png', 'type':'Honda Civic Front Kitti', \
               'car_id':9, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/toyota_camry_front_kitti.png', 'type': 'Toyota Camry Front Kitti', \
               'car_id':10, 'car_category': 'car', 'car_color': 'cream', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/toyota_prius_front_kitti.png', 'type': 'Toyota Prius Front Kitti', \
               'car_id':11,  'car_category': 'car', 'car_color': 'white', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/benz_front_kitti.png', 'type': 'Benz Front Kitti', \
               'car_id':12,  'car_category': 'car', 'car_color': 'white', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/ford_front_kitti.png', 'type': 'Ford Front Kitti', \
               'car_id':13,  'car_category': 'car', 'car_color': 'red', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/jeep_front_kitti.png', 'type': 'Jeep Front Kitti', \
               'car_id':14, 'car_category': 'jeep', 'car_color': 'red', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/jeep_cherokee_front_kitti.png', 'type': 'Jeep Cherokee Front Kitti', \
               'car_id':15, 'car_category': 'jeep', 'car_color': 'cream', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/fiat_front_kitti.png', 'type': 'Fiat Front Kitti', \
               'car_id':16, 'car_category': 'car', 'car_color': 'blue', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/bmw_front_kitti.png', 'type': 'BMW Front Kitti', \
               'car_id':17, 'car_category': 'car', 'car_color': 'blue dark', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/suzuki_front_kitti.png', 'type': 'Suzuki Front Kitti', \
               'car_id':18, 'car_category': 'jeep', 'car_color': 'red dark', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/volkswagen_golf_front_kitti.png', 'type': 'Volkswagen Golf Kitti', \
               'car_id':19, 'car_category': 'car', 'car_color': 'blue light', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/toyota_new_prius_front_kitti.png', 'type': 'Toyota New Prius Kitti', \
               'car_id':20, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/volvo_rear_kitti.png', 'type': 'Volvo Kitti', \
               'car_id':21, 'car_category': 'car', 'car_color': 'brown', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/porche_rear_kitti.png', 'type': 'Porche Kitti', \
               'car_id':22, 'car_category': 'car', 'car_color': 'white', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/corvette_front_kitti.png', 'type': 'Corvette Kitti', \
               'car_id':23, 'car_category': 'car', 'car_color': 'yellow', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/ford_truck_rear_kitti.png', 'type': 'Ford Kitti', \
               'car_id':24, 'car_category': 'truck', 'car_color': 'white', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/chevrolet_truck_rear_kitti.png', 'type': 'Chevrolet Kitti', \
               'car_id':25, 'car_category': 'truck', 'car_color': 'red', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/mercedes_rear_kitti.png', 'type': 'Mercedes Kitti', \
               'car_id':26, 'car_category': 'car', 'car_color': 'black', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/tesla_front_kitti.png', 'type': 'Tesla Kitti', \
               'car_id':27, 'car_category': 'car', 'car_color': 'black', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/mercedes_front_kitti.png', 'type': 'Mercedes Kitti', \
               'car_id':28, 'car_category': 'jeep', 'car_color': 'gray', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/mazda_front_kitti.png', 'type': 'Mazda Kitti', \
               'car_id':29, 'car_category': 'car', 'car_color': 'blue light', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/mazda_rear_kitti.png', 'type': 'Mazda Kitti', \
               'car_id':30, 'car_category': 'car', 'car_color': 'gray', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/scion_rear_kitti.png', 'type': 'Scion Kitti', \
               'car_id':31, 'car_category': 'car', 'car_color': 'orange', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/scion_front_kitti.png', 'type': 'Scion Kitti', \
               'car_id':32, 'car_category': 'car', 'car_color': 'orange', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/fiat_abarth_front_kitti.png', 'type': 'Fiat Abarth Kitti', \
               'car_id':33, 'car_category': 'car', 'car_color': 'orange', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/volkswagen_beetle_front_kitti.png', 'type': 'Volkswagen Beetle Kitti', \
               'car_id':34, 'car_category': 'car', 'car_color': 'red dark', 'car_orientation': FRONT_ORIENT },
              {'car_path': './pics/cars/smart_rear_kitti.png', 'type': 'Smart Kitti', \
               'car_id':35, 'car_category': 'car', 'car_color': 'black', 'car_orientation': BACK_ORIENT },
              {'car_path': './pics/cars/smart_front_kitti.png', 'type': 'Smart Kitti', \
               'car_id':36, 'car_category': 'car', 'car_color': 'blue light', 'car_orientation': FRONT_ORIENT }
              ]

configs_file = 'scene_configs_py2'

convert_sample_to_int = lambda sample, num_elems:  int(sample*(num_elems+1))


def update_library():
    Library = lib_object()
    with open(configs_file, 'rb') as f:
        configs = pickle.load(f)

    for i in range(len(road_images)):
        elem = configs[i]
        im_data = Image.open(road_images[i]['road_path'])
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
        im_data=Image.open(car['car_path'])
        Library.add_foregrounds(im_data=im_data,add_details=car)

    return Library
