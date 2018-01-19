import Point


class VoronoiCell(object):

	def __init__(self,pixelList,seedPoint):
		self.pixelList = pixelList
		self.seedPoint = seedPoint

	def findCentroid(self):
		##print(self.pixelList[0])
		xCenter = 0
		yCenter = 0
		totalPoints = len(self.pixelList)
		for z in range(len(self.pixelList)):
			xCenter +=self.pixelList[z].x 
			yCenter +=self.pixelList[z].y
		##print totalPoints
		if totalPoints == 0:
			totalPoints = 1
		xCenter = xCenter // totalPoints
		yCenter = yCenter // totalPoints

		centroid = Point.Point(xCenter,yCenter, self.seedPoint.color)
		##print ("Centroid is: " + str(centroid.x) + " " + str(centroid.y))
		return centroid