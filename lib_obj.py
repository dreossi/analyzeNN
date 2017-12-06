'''
This file defines the library
The library contains a list of background objects and foreground objects
'''

from im_obj import *

class lib_object():
    def __init__(self):
        self.background_objects = []
        self.foreground_objects = []

    def add_backgrounds(self, **kwargs):
        if 'back_obj' in kwargs:
            self.background_objects.append(kwargs['back_obj'])
        else:
            im_data = kwargs['im_data'] if 'im_data' in kwargs else None
            add_details = kwargs['add_details'] if 'add_details' in kwargs \
                    else None
            im_path = kwargs['im_path'] if 'im_path' in kwargs else None
            back_obj = back_object(im_data=im_data, add_details=add_details,
                                   im_path=im_path)
            self.background_objects.append(back_obj)

        scaling = kwargs['scale'] if 'scale' in kwargs else None
        if self.background_objects[-1].bounding_boxes is None:
            if 'bounding_boxes' in kwargs:
                self.background_objects[-1].update_sample_box(\
                    kwargs['bounding_boxes'], scale=scaling)
            else:
                None
                #print('Please update object with bounding box')

    def add_foregrounds(self, **kwargs):
        if 'fore_obj' in kwargs:
            self.foreground_objects.append(kwargs['fore_obj'])
        else:
            im_data = kwargs['im_data'] if 'im_data' in kwargs else None
            add_details = kwargs['add_details'] if 'add_details' in kwargs \
                else None
            im_path = kwargs['im_path'] if 'im_path' in kwargs else None
            fore_obj = fore_object(im_data=im_data, add_details=add_details,
                                   im_path=im_path)
            self.foreground_objects.append(fore_obj)


    def get_obj(self, type, id):
        if type == 'background':
            return self.background_objects[id]
        else:
            return self.foreground_objects[id]
