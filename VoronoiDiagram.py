import pygame, sys, random
import VoronoiCell as cell
import pytess

pygame.init()

class VoronoiDiagram(object):

	def __init__(self):
		##User input to decide number of cells
		self.numPoints = int(raw_input("Input number of cells: "))
		self.LENGTH = 950
		self.WIDTH = 900 
		self.cells = None
		self.seeds = None
		self.SCREEN = None

	##Creates white screen and makes random seeds
	def createScreen(self):
		## Sets screen size
		self.SCREEN = pygame.display.set_mode((self.LENGTH,self.WIDTH))
		## Make screen background white
		self.SCREEN.fill((255,255,255))

		## Seed screen and save seeds in list
		self.seeds = self.makeSeeds(self.numPoints,self.SCREEN)
		## Updates screen to show seeds
		pygame.display.update()
		return

	## Uses seeds to create voronoi diagram and update screen
	def createDiagram(self):
		diagram = pytess.voronoi(self.seeds)
		allCells = []
		##print(diagram)

		for i in range(len(diagram)):
			## diagram[i][0] contains seedPoint for polygon
			## diagram[i][1] contains all vertices for polygon i
			myCell = cell.VoronoiCell(diagram[i][0], diagram[i][1])
			allCells.append(myCell)
			##print (diagram[i][1])
			pygame.draw.polygon(self.SCREEN,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),diagram[i][1],0)

		pygame.display.update()
		## Saves cells within VoronoiDiagram cells attribute
		self.cells = allCells
		##pygame.image.save(SCREEN, "F:/Projects/voronoiMap/" + str(self.numPoints) + "diagram_start.jpeg")

		return

	##Randomly determines seed corrdinates
	## returns list of objects and coordinates
	def makeSeeds(self, numPoints,screen):
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
			screen.set_at((xVal, yVal),((0,0,0)))
		return seedCoordinates


		



