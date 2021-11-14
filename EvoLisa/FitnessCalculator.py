import pygame
import Tools
from pygame.locals import *

def GetDrawingFitness(g,pa):
	error = 0

	s = pygame.surfarray.array3d(g)

	x = 0
	y = 0

	for p in pa:
		r = int(s[x,y,0]) - int(p[0])
		g = int(s[x,y,1]) - int(p[1])
		b = int(s[x,y,2]) - int(p[2])
		pixelError = r*r+g*g+b*b
		error = error + pixelError
		x = x + 1
		if x >= Tools.MaxWidth:
			y = y + 1
			x = 0

	return error

