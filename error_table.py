'''
This file defines the error table object
'''

empty_elem = 'n/a'

class error_table():
    def __init__(self, **kwargs):
        if 'keys' in kwargs:
            print('Initializing the error table with the following elements: ')
            print(kwargs['keys'])
            self.entries = dict.fromkeys(kwargs['keys'], [])
        else:
            self.entries = {}
        self.num_elems = 0

    def update_with_elem(self, new_dict):
        # First update the common keys
        common_keys = set(new_dict.keys()) & set(self.entries.keys())
        for k in common_keys:
            self.entries[k].append(new_dict[k])

        # Second update the entries which are not present in the new dict
        absent_keys = set(self.entries.keys()) - set(new_dict.keys())
        for k in absent_keys:
            self.entries[k].append(empty_elem)

        # Third compute the keys that are not already present in entries
        missing_keys = set(new_dict.keys()) - set(self.entries.keys())
        for k in missing_keys:
            self.entries[k] = [empty_elem]*self.num_elems + [new_dict[k]]

        self.num_elems += 1



