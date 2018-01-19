import math,pygame
import sys
pygame.init()
##import numpy

class Point(object):

	def __init__(self,x,y, color):
		self.x = x
		self.y = y
		self.color = color

	## Determines the distance between two points
	def distance(self, otherPoint):
		xDiff = (self.x - otherPoint.x)**2
		yDiff = (self.y - otherPoint.y)**2
		totalDist = math.sqrt(xDiff + yDiff)
		return totalDist
		
	## Returns the index from seedList of the closest seedpoint.
	## Assigns point to color associated to closest seedPoint
	def closePoint(self,disList,seedList):
		minInd = disList.index(min(disList))
		self.color = seedList[minInd].color
		return minInd
