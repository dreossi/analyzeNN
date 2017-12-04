from scipy import spatial
import numpy as np

class KDTree:

    tree = None

    def __init__(self,data=[]):
        '''Initialize kdtree'''
        self.tree = spatial.KDTree(data)

    def dim(self, pt):
        '''Data dimensions'''
        return self.tree.data.shape

    def add(self, pt):
        '''Add point (in a very inefficient way)'''
        self.tree = spatial.KDTree(np.append(self.tree.data,[pt],axis=0))

    def query(self, pt):
        '''Distance and closest neighbor'''
        dist, neigh_idx = self.tree.query(pt)
        return dist, self.tree.data[neigh_idx]

    def esp_distant(self, pt, eps, add=False):
        '''Check if pt is eps distant from stored points'''
        dist, _  = self.tree.query(pt)
        eps_dist = dist >= eps
        if( eps_dist and add ):
            self.add(pt)
        return eps_dist, dist
