import pygame, sys, random
from noise import pnoise2
import VoronoiDiagram
pygame.init()

class Map(object):

	def __init__(self):
		## Creates VoronoiDiagram Object
		self.vDiagram = VoronoiDiagram.VoronoiDiagram()
		## Calls method to form and seed screen
		self.vDiagram.createScreen()
		## Calls method to create diagram from seeds
		self.vDiagram.createDiagram()
		## Calls method to smooth cells in diagram
		for i in range(2):
			self.vDiagram.smoothCells()

		for i in range(len(self.vDiagram.cells)):
			if self.vDiagram.cells[i].seedPoint != None and len(self.vDiagram.cells[i].vertices) > 2 :
					#if self.vDiagram.cells[i].seedPoint == None:
					#	pygame.draw.polygon(self.vDiagram.SCREEN,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),self.vDiagram.cells[i].vertices,0)
					#baseNoise =perlin.BaseNoise()
					#generator = perlin.SimplexNoise(baseNoise)
					
					noiseVal  = pnoise2((self.vDiagram.cells[i].seedPoint[0] + random.randint(0,250))/ 750.0,
						(self.vDiagram.cells[i].seedPoint[1] + random.randint(0,250))/ 750.0)
					
					noiseVal = (noiseVal+1)/2
					
					if noiseVal < 1 and noiseVal >= .50:
						pygame.draw.polygon(self.vDiagram.SCREEN,(0,255*noiseVal,255*noiseVal),self.vDiagram.cells[i].vertices,0)
					elif noiseVal < .60 and noiseVal >= 0:
						pygame.draw.polygon(self.vDiagram.SCREEN,(0,255*noiseVal,0),self.vDiagram.cells[i].vertices,0)
					#pygame.draw.polygon(self.vDiagram.SCREEN,(0,205,255),self.vDiagram.cells[i].vertices,0)
					##print self.vDiagram.cells[i].vertices
					#print self.vDiagram.delauney
					#pygame.draw.lines(self.vDiagram.SCREEN,(0,0,0),False,self.vDiagram.delauney[0])
		pygame.display.update()
		pygame.image.save(self.vDiagram.SCREEN, str(self.vDiagram.numPoints) + "diagram.jpeg")

