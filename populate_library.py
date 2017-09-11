# Filling up the Library with the roads and cars


from PIL import Image, ImageDraw
# from scipy import misc
# from collections import namedtuple
from components import ImageFile
from library import *
# import numpy as np
# from ml_primitives import uniform_sampling
from gen_pic_utils import coord, rect, scale_image, fit_image, generateImage, shift_xz, modifyImageLook, cluster_in_abstract

def populateLibrary():
    # Create a Library
    Lib = library()

    # Populate the library with roads
    Lib.addRoad(ImageFile(Image.open("./pics/roads/desert.jpg"), "Desert Road"), coord(800, 540), coord(100, 950), coord(1500,950), [coord(800,950)])
    Lib.addRoad(ImageFile(Image.open("./pics/roads/countryside.jpg"), "Countryside Road"), coord(810, 540),coord(100, 1000), coord(1500, 1000), [coord(775,1000)])
    Lib.addRoad(ImageFile(Image.open("./pics/roads/city.jpg"), "City Road"), coord(810, 675), coord(100, 925), coord(1500, 925), [coord(508, 925), coord(1025, 925)])
    Lib.addRoad(ImageFile(Image.open("./pics/roads/cropped_desert.jpg"), "Cropped Desert Road"), coord(75, 120), coord(100,500), coord(1400, 500), [coord(66,500)])

    for i in range(134,182):
        Lib.addRoad(ImageFile(Image.open("./pics/roads/forest/0000000" + str(i) + ".png"), "Forest Road"), coord(675, 238),
                    coord(80, 500), coord(840, 504), [coord(340, 499)])


    # vanishing point, low-left, low-right, center line
    Lib.addRoad(ImageFile(Image.open("./pics/roads/desert_kitti.png"), "Desert Road"), coord(621, 208), coord(336, 344), coord(920,344), [coord(618,344)])      #52
    Lib.addRoad(ImageFile(Image.open("./pics/roads/city_kitti.png"), "City Road"), coord(630, 150), coord(336, 344), coord(920,344), [coord(618,344)])          #53
    Lib.addRoad(ImageFile(Image.open("./pics/roads/forest_kitti.png"), "Forest Road"), coord(672, 238), coord(200, 430), coord(656,430), [coord(436,430)])      #54
    Lib.addRoad(ImageFile(Image.open("./pics/roads/big_sur_kitti.png"), "Big Sur Road"), coord(746,90), coord(470, 268), coord(1072,268), [coord(753,268)])     #55
    Lib.addRoad(ImageFile(Image.open("./pics/roads/mountain_kitti.jpg"), "Mountain Road"), coord(678,106), coord(330, 299), coord(960,299), [coord(635,960)])   #56
    Lib.addRoad(ImageFile(Image.open("./pics/roads/bridge_kitti.jpg"), "Bridge Road"), coord(627,105), coord(399, 254), coord(900,254), [coord(629,254)])       #57
    Lib.addRoad(ImageFile(Image.open("./pics/roads/tunnel_kitti.jpg"), "Tunnel Road"), coord(651, 163), coord(363, 328), coord(826, 328), [coord(622, 328)])    #58
    Lib.addRoad(ImageFile(Image.open("./pics/roads/island_kitti.jpg"), "Island Road"), coord(616, 179), coord(386, 315),coord(864, 315), [coord(607, 315)])     #59
    Lib.addRoad(ImageFile(Image.open("./pics/roads/countryside_kitti.jpg"), "Country Road"), coord(627, 146), coord(462, 306),coord(785, 306), [coord(621, 306)])   # 60
    Lib.addRoad(ImageFile(Image.open("./pics/roads/hill_kitti.jpg"), "Hill Road"), coord(613, 166),coord(382, 314), coord(846, 314), [coord(617, 314)])         # 61
    Lib.addRoad(ImageFile(Image.open("./pics/roads/alps_kitti.png"), "Alps Road"), coord(613, 166),coord(382, 314), coord(846, 314), [coord(617, 314)])




    # Populate the library with cars
    Lib.addCar(ImageFile(Image.open("./pics/cars/bmw_rear.png"), "BMW"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/tesla_rear.png"), "Tesla"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/suzuki_rear.png"), "Suzuki"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/modified_bmw.png"), "Modified BMW"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/bmw_kitti.png"), "BMW Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/suzuki_kitti.png"), "Suzuki Kitti"))                    #5
    Lib.addCar(ImageFile(Image.open("./pics/cars/tesla_kitti.png"), "Tesla Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/fiat_kitti.png"), "Fiat Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/honda_kitti.png"), "Honda Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/toyota_kitti.png"), "Toyota Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/peugeot_kitti.png"), "Peugeot Kitti"))                  #10
    Lib.addCar(ImageFile(Image.open("./pics/cars/chrysler_kitti.png"), "Chrysler Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/bmw_blue_kitti.png"), "BMW Blue Kitti"))

    Lib.addCar(ImageFile(Image.open("./pics/cars/honda_civic_front_kitti.png"), "Honda Civic Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/toyota_camry_front_kitti.png"), "Toyota Camry Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/toyota_prius_front_kitti.png"), "Toyota Prius Kitti"))  #15
    Lib.addCar(ImageFile(Image.open("./pics/cars/benz_front_kitti.png"), "Benz Mercedes Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/ford_front_kitti.png"), "Ford Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/jeep_front_kitti.png"), "Jeep Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/jeep_cherokee_front_kitti.png"), "Jeep Cherokee Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/fiat_front_kitti.png"), "Fiat Kitti"))                  #20
    Lib.addCar(ImageFile(Image.open("./pics/cars/bmw_front_kitti.png"), "BMW Kitti"))
    Lib.addCar(ImageFile(Image.open("./pics/cars/suzuki_front_kitti.png"), "Suzuki Kitti"))

    return Lib
