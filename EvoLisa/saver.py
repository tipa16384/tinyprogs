from copy import deepcopy
import pygame
from pygame.locals import *
import random
from time import time

###############################################################
#	Picture
#		class containing picture information
#		test!
###############################################################

class Picture:
	def __init__(self,fn):
		print "Picture: creating Picture for %s" % (fn)
		self.path = "C:/Users/brenda/progs/EvoLisa/"
		self.fn = fn
		self.rect = pygame.Rect(0,0,0,0)
		self.image = None
		self.pa = []
		self.white = pygame.Color('white')
		self.load()
		
	def load(self):
		print "Picture: loading %s" % (self.fn)
		self.image = pygame.image.load(self.path+self.fn)
		self.rect = self.image.get_rect()
		print "--- successfully loaded, rect is %s" % (self.rect)
		self.pa = range(self.rect.h*self.rect.w)
		i = 0
		for y in range(self.rect.h):
			for x in range(self.rect.w):
				self.pa[i] = self.image.get_at((x,y))
				i = i + 1
		print "--- array made %s" % (self.rect)
		
	def colorAt(self,x,y):
		if x >= self.rect.w or y >= self.rect.h:
			return self.white
		return self.pa[y*self.rect.w+x]

	def convert(self):
		print "Picture: convert %s" % (self.fn)
		self.image = self.image.convert()

###############################################################
#	Saver
#		main class
###############################################################

class Saver:
	def __init__(self):
		print "Saver: initializing..."
		pygame.init()
		self.imageFiles = ['blueridge.jpg','chair.jpg','clouds.jpg','flowers.jpg','lake.jpg','monopoly.jpg','mutual.jpg','nieces.jpg','skyline.jpg','staunton.jpg']
		self.lspread = 10
		self.hspread = 50
		self.surfaceHash = {}
		self.chroma = pygame.Color("white")
		self.images = []
		self.rect = pygame.Rect(0,0,0,0)
		self.screen = None
		self.dot = None
		
	def loadImages(self):
		print "-- Saver.loadImages"
		for p in self.imageFiles:
			pc = Picture(p)
			self.images.append(pc)
			self.rect = pygame.Rect(0,0,max(self.rect.w,pc.rect.w),max(self.rect.h,pc.rect.h))
			
	def initScreen(self):
		print "-- Saver.initScreen"
		self.screen = pygame.display.set_mode((self.rect.w,self.rect.h))
		dot = pygame.Surface((self.hspread,self.hspread))
		dot = dot.convert()
		dot.set_colorkey(self.chroma)

		self.screen.fill(self.chroma)
		pygame.display.flip()

		for i in range(self.lspread,self.hspread+1):
			dot = pygame.Surface((i,i))
			dot = dot.convert()
			dot.set_colorkey(self.chroma)
			self.surfaceHash[i] = dot

	def process(self):
		print "-- Saver: process"
		
		for pc in self.images:
			pc.convert()
			
		pc = self.images[0]
		
		while True:
			for pc in self.images:
				for generation in range(300000):
					spr = random.randint(self.lspread,self.hspread)
					x = random.randint(0,self.rect.w-spr)
					y = random.randint(0,self.rect.h-spr)
			
					color = pc.colorAt(x,y)
		
					#dot = self.surfaceHash[spr]
					#dot.set_alpha(255)
					#dot.fill(self.chroma)
					#pygame.draw.ellipse(dot,color,dot.get_rect())
					#self.screen.blit(dot,(x,y))
					pygame.draw.ellipse(self.screen,color,Rect((x-self.hspread/2,y-self.hspread/2),(self.hspread,self.hspread)))

					if (generation % 1000) == 0:
						if (generation % 10000) == 0 and self.hspread > self.lspread:
							self.hspread = max(self.lspread,self.hspread - 5)
						pygame.display.flip()
						#print "%d generation-%d" % (self.hspread,generation)
	
###############################################################
#	main
#		do stuff
###############################################################

saver = Saver()
saver.loadImages()
saver.initScreen()
saver.process()
