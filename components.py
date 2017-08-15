# This file defines class objects for Roads, Sceneries and Cars.

from collections import namedtuple

ImageFile = namedtuple('ImageFile', 'data description')

class road():
	def __init__(self, ImageFile, vp, min_x, max_x, lanes):
		self.componentType = 'Road'
		self.data = ImageFile.data
		self.description = ImageFile.description
		self.vp = vp
		self.min_x = min_x
		self.max_x = max_x
		self.lanes = lanes

	def __repr__(self):
		return "Picture : " + self.description


class car():
	def __init__(self, ImageFile):
		self.componentType = 'Car'
		self.data = ImageFile.data
		self.description = ImageFile.description

	def __repr__(self):
		return "Picture : " + self.description
