# object.py

from pygame.image import *
from pygame.transform import *
from pygame.sprite import DirtySprite
from pygame import Rect

from medialibrary import getMedia
from gamevars import *
from random import randint
import os

class Object(DirtySprite):
	def __init__(self):
		DirtySprite.__init__(self)
		self.dirty = 2
		self.pos = (0,0)
		self.identified = False
		self.needsIdentification = True
		self.desc = "Object"
		self.ldesc = "an object"
		self.setType(O_GENERIC)
		self.media = None
		self.direction = N
		self.targeted = False

		self.rotations = {N:None, E:None, W:None, S:None, NE:None, NW:None, SE:None, SW:None}
		
		# place the object anywhere by default
		self.setPosRandom()
	
	def canBeTargeted(self):
		return self.otype < O_TARGET 
	
	def getDir(self):
		return self.direction
	
	def setDir(self,facing):
		self.direction = facing

	def setImageName(self,name):
		self.media = getMedia(name)
	
	def setDir(self,facing):
		self.direction = facing

	def setPosRandom(self):
		self.pos = (randint(1,ROOMW-2),randint(1,ROOMH-2))
		
	def setPos(self,pos):
		self.pos = pos
	
	def getPos(self):
		return self.pos
	
	def isIdentified(self):
		return self.identified
	
	def setIdentified(self,flag):
		self.identified = flag
	
	def isNeedsID(self):
		return self.needsIdentification
	
	def setNeedsID(self,flag):
		self.needsIdentification = flag
		
	def getDesc(self):
		return self.desc
	
	def setDesc(self,desc):
		self.desc = desc
	
	def getLDesc(self):
		return self.ldesc
	
	def setLDesc(self,desc):
		self.ldesc = desc
	
	def getType(self):
		return self.otype
	
	def setType(self,otype):
		self.otype = otype
	
	def update(self,scrollPos,board,player):
		"Object.update"
		self.image = self.media.getImage(self.direction)
		x = (self.pos[0]-scrollPos[0])*OSIZE+OSIZE/2
		y = (self.pos[1]-scrollPos[1])*OSIZE+OSIZE/2
		w = self.image.get_width()
		h = self.image.get_height()
		self.rect = Rect(x-w/2,y-h/2,w,h)
		
		if self.getType() > O_TARGET:
			self.visible = 1
		
		if self.getType() != O_PLAYER:
			spot = board.getAt(self.pos[0],self.pos[1])
			pspot = board.getAt(player.pos[0],player.pos[1])
			if spot.getCode() != pspot.getCode():
				#self.rect = Rect(-100,-100,0,0)
				self.visible = 0
