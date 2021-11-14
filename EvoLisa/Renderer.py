import pygame

# g is a pygame.Surface

chroma = pygame.Color("Black")

def Render(drawing,g,scale=1):
	g.fill(chroma)
	for polygon in drawing.polygons:
		polygon.render(g)

