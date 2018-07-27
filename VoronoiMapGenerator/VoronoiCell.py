

class VoronoiCell(object):

	def __init__(self,seedPoint,vertices):
		self.vertices = vertices
		self.seedPoint = seedPoint
		self.land = True

	def findCentroid(self):
		centroid = []
		centroidX = 0
		centroidY = 0
		for i in range(len(self.vertices)):
			centroidX += self.vertices[i][0]
			centroidY += self.vertices[i][1]
		centroidX = int(centroidX/(len(self.vertices)))
		centroidY = int(centroidY/(len(self.vertices)))
		centroid.append(centroidX)
		centroid.append(centroidY)
		
		return centroid