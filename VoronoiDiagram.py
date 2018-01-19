import pygame, sys, random
import Point, VoronoiCell
pygame.init()

class VoronoiDiagram(object):

	def __init__(self):
		##User input to decide number of cells
		self.numPoints = int(raw_input("Input number of cells: "))
		self.LENGTH = 750
		self.WIDTH = 700 
		self.cells = None
		self.seeds = None

	##Creates white screen and allows exit on clicking x
	def createScreen(self):
		## Sets screen size
		SCREEN = pygame.display.set_mode((self.LENGTH,self.WIDTH))
		## Make screen background white
		SCREEN.fill((255,255,255))
		## Seed screen and save seeds in list
		seedList = self.seedScreen(self.numPoints,SCREEN)
		## Find closest seed and set color to that seed color
		## Return list all pixels grouped based on their closest seed
		pixelDistr = self.closestSeed(seedList,SCREEN)
		## Return list of all cells
		cellList = self.defineCells(pixelDistr,seedList)

		##Set seeds to white
		for i in range(len(cellList)):
			##print (cellList[i].seedPoint.x)
			SCREEN.set_at((cellList[i].seedPoint.x,cellList[i].seedPoint.y),(250,250,250))

		pygame.image.save(SCREEN, str(self.numPoints) + "diagram_start.jpeg")

		##Relaxes cells in a loop
		for i in range(2):
			self.seeds = self.relaxCells(cellList,SCREEN)
		pygame.display.update()
		pygame.image.save(SCREEN, str(self.numPoints) + "diagram_relaxed2.jpeg")
		return SCREEN

	##Randomly chooses number of points and places them on screen. 
	##Returns list of seed coordinates
	def seedScreen(self, numPoints,screen):
		seeds = []
		for i in range(0,numPoints):
			## makes random color for the seedpoint object
			randColor = pygame.Color(random.randint(0,250),random.randint(0,250),random.randint(0,250))
			## makes seedpoint at random location
			myPoint = Point.Point(random.randint(0,self.LENGTH),random.randint(0,self.WIDTH), randColor)
			screen.set_at((myPoint.x, myPoint.y),((0,0,0)))
			seeds.append(myPoint)
		return seeds

	##Determines closest seed point
	def closestSeed(self,seedPointList, screen):
		##print (len(seedPointList))
		allPixel = [[] for i in range(len(seedPointList))]
		## Range of x coordinates 
		for i in range(0,self.LENGTH):
			## Range of y coordinates
			for q in range(0,self.WIDTH):
				pixel = Point.Point(i,q,None)

				seedDist = []
				## Range of seedPoints
				for z in range(0,len(seedPointList)):
					## Get distance from pixel to seed points and add them to seedDist list
					pixelDist = pixel.distance(seedPointList[z])
					seedDist.append(pixelDist)
				## Use seedDist to find closest seedPoint
				closeSeedInd = pixel.closePoint(seedDist,seedPointList)
				allPixel[closeSeedInd].append(pixel)
				screen.set_at((pixel.x,pixel.y),pixel.color)
		return allPixel

	def defineCells(self, pixelDistr, seedList):
		myCells = []
		for i in range(len(seedList)):
			cell = VoronoiCell.VoronoiCell(pixelDistr[i],seedList[i])
			##print ("SeedPoint is: " + str(cell.seedPoint.x) + " " + str(cell.seedPoint.y))
			myCells.append(cell)
		return myCells

	def relaxCells(self,cellList,screen):
		myCentroids = []
		for i in range(len(cellList)):
			centroid = cellList[i].findCentroid()
			myCentroids.append(centroid)
			screen.set_at((centroid.x,centroid.y),(0,0,0))
		## Find closest seed and set color to that seed color
		## Return list all pixels grouped based on their closest seed
		pixelDistr = self.closestSeed(myCentroids,screen)
		## Return list of all cells
		self.cells = self.defineCells(pixelDistr,myCentroids)
		for i in range(len(myCentroids)):
			##Set centroids to black 
			screen.set_at((myCentroids[i].x, myCentroids[i].y),((0,0,0)))
		return myCentroids

