# This file populates a library with instances of the component

import components as comp

class library:
	def __init__(self):
		self.roads = []
		self.cars = []

	def __repr__(self):
		return "Number of roads : " + str(len(self.roads)) + "\nNumber of cars : " + str(len(self.cars))

	def getElement(self, type, number):
		if type == "roads":
			return self.roads[number]
		elif type == "cars":
			return self.cars[number]
		else:
			return "Error: Search by either cars or roads"

	def addRoad(self, *args):
		self.roads.append(comp.road(*args))
		return

	def addCar(self, *args):
		self.cars.append(comp.car(*args))
		return
