import Map
import pygame
import sys

myMap = Map.Map()
myMap.vDiagram.createDiagram()
#myMap.findCenterCell()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
