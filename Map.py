import pygame, sys, random
import VoronoiDiagram
import Point
pygame.init()

class Map(object):

	def __init__(self):
		self.vDiagram = VoronoiDiagram.VoronoiDiagram()
		self.vDiagram.createScreen()

	# def findCenterCell(self ):
	# 	#self.diagram.seeds
	# 	#self.diagram.cells
	# 	cells = self.diagram.cells
	# 	center = Point.Point(self.diagram.LENGTH/2,self.diagram.WIDTH/2,None)
	# 	orderCells = sorted(cells, key=lambda p: p.seedPoint.distance(center))
	# 	#for i in range(len(cells)):
	# 	#	print cells[i].seedPoint.x, cells[i].seedPoint.y

	# 	R = 250.0
	# 	G = 250.0
	# 	B = 250.0
	# 	for n in range(len(orderCells)):
	# 		for i in range(len(orderCells[n].pixelList)):
	# 			self.SCREEN.set_at((orderCells[n].pixelList[i].x,orderCells[n].pixelList[i].y),((R,G,B)))
			
	# 			##print (R,G,B)
	# 			##print (float(1/5))
	# 		if R >= 10 and B>=10:
	# 			R -=1200.0/float(len(cells))
	# 			B -=1200.0/float(len(cells))
	# 		elif G >=90 :
	# 			G -=500.0/float(len(cells))
	# 		elif R<10 and B<10 and G<90:
	# 			B =250
	# 			#orderCells[0].pixelList[i].color = pygame.Color(250,250,250)
	# 	pygame.display.update()
	# 	pygame.image.save(self.SCREEN, str(self.diagram.numPoints) + "diagram_altitude.jpeg")


