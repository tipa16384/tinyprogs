import Tools, Settings
from copy import deepcopy
import pygame
import FitnessCalculator
from pygame.locals import *
import random
from time import time

imageFile = 'bear.jpg'

legalColors = [(215,26,33,255),(0,50,77,255),(113,150,159,255),(252,228,168,255),(161,190,168,255)]

spread = 5
polyNumber = 0
surfaceHash = {}
chroma = pygame.Color("White")

class DnaDrawing:
	def __init__(self):
		self.dirty = False
		self.polygons = []
		self.pointCount = 0
		for i in range(Settings.activePolygonsMin):
			self.addPolygon()
		print "%d polygons" % (len(self.polygons))
		self.calcPointCount()
		self.setDirty()

	def draw(self,screen):
		screen.fill(chroma)
		for p in self.polygons:
			p.render(screen)

	def setDirty(self):
		self.dirty = True

	def calcPointCount(self):
		self.pointCount = sum([len(p.points) for p in self.polygons])

	def clearDirty(self):
		if self.dirty:
			self.dirty = False
			self.calcPointCount()

	def clone(self):
		return deepcopy(self)

	def mutate(self):
		if Tools.WillMutate(Settings.activeAddPolygonMutationRate):
			self.addPolygon()

		if Tools.WillMutate(Settings.activeRemovePolygonMutationRate):
			self.removePolygon()

		if Tools.WillMutate(Settings.activeMovePolygonMutationRate):
			self.movePolygon()

		for p in self.polygons:
			p.mutate(self)

		if self.dirty:
			self.calcPointCount()

	def movePolygon(self):
		if len(self.polygons) < 2:
			return
		p = random.choice(self.polygons)
		self.polygons.remove(p)
		i = random.randint(0,len(self.polygons)-1)
		self.polygons.insert(i,p)
		self.setDirty()

	def removePolygon(self):
		if len(self.polygons) > Settings.activePolygonsMin:
			p = random.choice(self.polygons)
			self.polygons.remove(p)
			self.setDirty()

	def addPolygon(self):
		if len(self.polygons) < Settings.activePolygonsMax:
			newPolygon = DnaPolygon()
			if len(self.polygons) > 1:
				i = random.randint(0,len(self.polygons)-1)
				self.polygons.insert(i,newPolygon)
			else:
				self.polygons.append(newPolygon)
			self.setDirty()

class DnaPoint:
	def __init__(self):
		self.x = random.randint(0,Tools.MaxWidth-1)
		self.y = random.randint(0,Tools.MaxHeight-1)

	def clone(self):
		return deepcopy(self)

	def mutate(self,drawing):
		mutated = False
		if Tools.WillMutate(Settings.activeMovePointMaxMutationRate):
			self.x = Tools.GetRandomNumber(0, Tools.MaxWidth-1)
			self.y = Tools.GetRandomNumber(0, Tools.MaxHeight-1)
			drawing.setDirty()
			mutated = True

		if Tools.WillMutate(Settings.activeMovePointMidMutationRate):
			self.x = min(max(0,self.x+Tools.GetRandomNumber(-Settings.activeMovePointRangeMid,Settings.activeMovePointRangeMid)), Tools.MaxWidth-1)
			self.y = min(max(0,self.y+Tools.GetRandomNumber(-Settings.activeMovePointRangeMid,Settings.activeMovePointRangeMid)), Tools.MaxHeight-1)
			drawing.setDirty()
			mutated = True

		if Tools.WillMutate(Settings.activeMovePointMinMutationRate):
			self.x = min(max(0,self.x+Tools.GetRandomNumber(-Settings.activeMovePointRangeMin,Settings.activeMovePointRangeMin)),Tools.MaxWidth-1)
			self.y = min(max(0,self.y+Tools.GetRandomNumber(-Settings.activeMovePointRangeMin,Settings.activeMovePointRangeMin)),Tools.MaxHeight-1)
			drawing.setDirty()
			mutated = True

		return mutated

class DnaPolygon:
	def __init__(self):
		global polyNumber
		self.points = []
		self.brush = DnaBrush()
		self.number = polyNumber
		polyNumber = polyNumber + 1

		origin = DnaPoint()
		
		for i in range(Settings.activePointsPerPolygonMin):
			point = DnaPoint()
			point.x = min(max(0,origin.x+Tools.GetRandomNumber(-spread, spread)),Tools.MaxWidth-1)
			point.y = min(max(0,origin.y+Tools.GetRandomNumber(-spread, spread)),Tools.MaxHeight-1)
			self.points.append(point)

	def clone(self):
		return deepcopy(self)

	def mutate(self,drawing):
		mutated = False

		if Tools.WillMutate(Settings.activeAddPointMutationRate):
			self.addPoint(drawing);

		if Tools.WillMutate(Settings.activeRemovePointMutationRate):
			self.removePoint(drawing);
		
		if self.brush.mutate(drawing):
			mutated = True

		for p in self.points:
			if p.mutate(drawing):
				mutated = True
		
		if mutated:
			global polyNumber
			self.number = polyNumber
			polyNumber = polyNumber + 1
				

	def render(self,screen):
		global surfaceHash

		if surfaceHash.has_key(self.number):
			g = surfaceHash[self.number]
			screen.blit(g,(self.x1,self.y1))
			return

		if len(self.points) > 0:
			p = self.points[0]
			self.x1 = p.x
			x2 = p.x
			self.y1 = p.y
			y2 = p.y
			for p in self.points[1:]:
				self.x1 = min(self.x1,p.x)
				x2 = max(x2,p.x)
				self.y1 = min(self.y1,p.x)
				y2 = max(y2,p.x)
			w = x2 - self.x1
			h = y2 - self.y1
			g = pygame.Surface((w,h))
			g = g.convert()
			g.fill(chroma)
			g.set_colorkey(chroma)
			g.set_alpha(self.brush.color[3])
			
			if len(surfaceHash) > 500:
				surfaceHash = {}

			surfaceHash[self.number] = g

			z = []
			for p in self.points:
				z.append((p.x-self.x1,p.y-self.y1))
			pygame.draw.polygon(g,self.brush.color,z)

			try:	
				screen.blit(g,(self.x1,self.y1))
			except Exception,e:
				print "blit failure:",e
				print "coords ",(self.x1,self.y1)

	def removePoint(self,drawing):
		if len(self.points) > Settings.activePointsPerPolygonMin:
			if drawing.pointCount > Settings.activePointsMin:
				self.points.remove(random.choice(self.points))
				drawing.setDirty()

	def addPoint(self,drawing):
		if len(self.points) < Settings.activePointsPerPolygonMax:
			if drawing.pointCount < Settings.activePointsMax:
				newPoint = DnaPoint()
				index = random.randint(1,len(self.points)-1)
				prev = self.points[index-1]
				next = self.points[index]
				newPoint.x = (prev.x+next.x)/2
				newPoint.y = (prev.y+next.y)/2
				self.points.insert(index,newPoint)
				drawing.setDirty()


class DnaBrush:
	def __init__(self):

		#red = Tools.GetRandomNumber(0, 255)
		#green = Tools.GetRandomNumber(0, 255)
		#blue = Tools.GetRandomNumber(0, 255)
		#alpha = Tools.GetRandomNumber(Settings.activeAlphaRangeMin, Settings.activeAlphaRangeMax)
		self.color = random.choice(legalColors)
		#self.color = (red,green,blue,alpha)

	def clone(self):
		return deepcopy(self)

	def mutate(self,drawing):
		mutated = False
		red = self.color[0]
		green = self.color[1]
		blue = self.color[2]
		alpha = self.color[3]

		if Tools.WillMutate(Settings.activeRedMutationRate):
			red = Tools.GetRandomNumber(Settings.activeRedRangeMin, Settings.activeRedRangeMax)
			drawing.setDirty()
			mutated = True

		if Tools.WillMutate(Settings.activeGreenMutationRate):
			green = Tools.GetRandomNumber(Settings.activeGreenRangeMin, Settings.activeGreenRangeMax)
			drawing.setDirty()
			mutated = True

		if Tools.WillMutate(Settings.activeBlueMutationRate):
			blue = Tools.GetRandomNumber(Settings.activeBlueRangeMin, Settings.activeBlueRangeMax)
			drawing.setDirty()
			mutated = True

		if Tools.WillMutate(Settings.activeAlphaMutationRate):
			alpha = Tools.GetRandomNumber(Settings.activeAlphaRangeMin, Settings.activeAlphaRangeMax)
			drawing.setDirty()
			mutated = True

		if mutated:
			#self.color = (red,green,blue,alpha)
			self.color = random.choice(legalColors)
			self.color = (self.color[0],self.color[1],self.color[2],alpha)
		return mutated

def Main():
	global chroma

	pygame.init()
	
	Settings.activePolygonsMin = 20

	image = pygame.image.load(imageFile)
	r = image.get_rect()
	sr = image.get_rect()
	if r.w > r.h:
		sr.h = 2*sr.h
		imagexy = (0,r.h)
	else:
		sr.w = 2*sr.w
		imagexy = (r.w,0)

	screen = pygame.display.set_mode((sr.w,sr.h))
	xscreen = pygame.Surface((r.w,r.h))
	image = image.convert()
	#chroma = image.get_at((r.w/2,r.h/2))
	#chroma = pygame.Color("Black")
	print "chroma color",chroma
	Tools.MaxWidth = r.w
	Tools.MaxHeight = r.h
	drawing = DnaDrawing()
	drawing.draw(screen)
	generation = 0
#	screen.blit(xscreen,(0,0))
	screen.blit(image,imagexy)
	pygame.display.flip()

	imagePixels = []

	for y in range(r.h):
		for x in range(r.w):
			color = image.get_at((x,y))
			imagePixels.append(color)

	best = FitnessCalculator.GetDrawingFitness(screen,imagePixels)

	tries = 0
	gtime = time()

	while generation < 10000:
		ndraw = deepcopy(drawing)
		ndraw.dirty = False
		while not ndraw.dirty:
			ndraw.mutate()
		tries = tries + 1
		ndraw.draw(screen)
		error = FitnessCalculator.GetDrawingFitness(screen,imagePixels)
		if error < best:
			#print "error",error
			best = error
			drawing = ndraw
		else:
			continue
		screen.blit(screen,(0,0))
		screen.blit(image,imagexy)
		pygame.display.flip()
		if (generation % 100) == 0:
			print "generation",generation
			ntime = time()
			if ntime != gtime and tries > 0:
				print "%f tries/second" % (tries/(ntime-gtime))
			tries = 0
			fn = imageFile.split('.')
			fn = "%s.%s" % (fn[0],"tga")
			pygame.image.save(screen,fn)
			gtime = time()
		generation = generation + 1

Main()

