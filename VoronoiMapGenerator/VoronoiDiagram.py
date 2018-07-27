import pygame, sys, random
import VoronoiCell as cell
import pytess

pygame.init()

class VoronoiDiagram(object):

	def __init__(self):
		##User input to decide number of cells
		self.numPoints = 250
		self.LENGTH = 950
		self.WIDTH = 950 
		self.cells = None
		self.seeds = None
		self.SCREEN = None
		self.delauney = None

	##Creates white screen and makes random seeds
	def createScreen(self):
		## Sets screen size
		self.SCREEN = pygame.display.set_mode((self.LENGTH,self.WIDTH))

		## Seed screen and save seeds in list
		self.seeds = self.makeSeeds(self.numPoints,self.SCREEN)
		## Updates screen to show seeds
		##pygame.display.update()
		return

	##Randomly determines seed corrdinates
	## returns list of objects and coordinates
	def makeSeeds(self, numPoints, screen):
		seedCoordinates = []

		for i in range(0,numPoints):
			coordinates = []
			## makes random x and y value for corrdinates
			xVal = random.randint(0,self.LENGTH)
			yVal = random.randint(0,self.WIDTH)

			coordinates.append(xVal)
			coordinates.append(yVal)
			## Adds coordinates to seeds list
			seedCoordinates.append(coordinates)

			## Sets seedPoints to black on screen
			##screen.set_at((xVal, yVal),((0,0,0)))
		return seedCoordinates

	## Uses seeds to create diagram with pytess
	def createDiagram(self):

		diagram = pytess.voronoi(self.seeds)
		self.makeCells(diagram)

		self.delauney = pytess.triangulate(self.seeds)
		
		return

	## Determines centroid of cells 
	## Uses centroids as seeds for new iteration of diagram
	def smoothCells(self):
		newSeedList = []
		for i in range(len(self.cells)):
			centroid = self.cells[i].findCentroid()
			newSeedList.append(centroid)
			#print centroid[0]
			#print centroid[1]
			#if centroid[0] < 0 or centroid[1] < 0:
			#	self.cells[i].land = False
			#	print self.cells[i].land

		##	self.SCREEN.set_at((centroid[0],centroid[1]),((250,0,0)))
		self.seeds = newSeedList
		self.createDiagram()


	## Creates VoronoiCell object for each set of vertices and seed points
	## Adds cell objects to array and sets array to self.cells for ease of access
	def makeCells(self, diagram):
		allCells = []
		for i in range(len(diagram)):
			## diagram[i][0] contains seedPoint for polygon
			## diagram[i][1] contains all vertices for polygon i
			myCell = cell.VoronoiCell(diagram[i][0], diagram[i][1])
			allCells.append(myCell)
			##print (diagram[i][1])
			#if len(diagram[i][1]) > 2 :
			#	pygame.draw.polygon(self.SCREEN,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),diagram[i][1],0)

		## Saves cells within VoronoiDiagram cells attribute
		self.cells = allCells