from scipy import spatial
import numpy as np

class ConfigDB:

    data = None

    def __init__(self):
        self.data = []


    def dim(self):
        '''Data dimension'''
        return len(self.data)


    def add(self, conf):
        '''Add config'''
        self.data += [conf]


    def dist(self, conf1, conf2):
        '''Get distance'''
        d = 0
        # Background
        if conf1[0] != conf2[0]:
            d = d + 1

        # Car models
        d = d + np.equal(conf1[1:4],conf2[1:4]).tolist().count(False)

        # All the rest
        d = d + np.linalg.norm(np.array(conf1[4:])-np.array(conf2[4:]))

        return d


    def dist_closest_neigh(self, conf):
        '''Distance from closest stored point'''
        min_dist = 999
        for dt in self.data:
            d = self.dist(dt,conf)
            if d < min_dist:
                min_dist = d
        return min_dist


    def eps_dist(self, conf, eps):
        '''Is conf eps-distant from stored points?'''
        for dt in self.data:
            if self.dist(dt,conf) < eps:
                return False
        return True


    def print_data(self):
        '''Print stored data'''
        for d in self.data:
            print(d)
