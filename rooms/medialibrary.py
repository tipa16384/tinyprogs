# medialibrary.py

from pygame.image import *
from pygame.transform import *
from pygame.sprite import Sprite
from pygame import Rect

from gamevars import *
from random import randint
import os


_library = {}

def getMedia(fn):
	if fn in _library:
		return _library[fn]
	
	m = Media()
	m.setImageName(fn)
	m.loadImage()
	_library[fn] = m
	return m


class Media:
	def __init__(self):
		self.imageFileName = ''
		self.srcImage = None
		self.rotations = {N:None, E:None, W:None, S:None, NE:None, NW:None, SE:None, SW:None}

	def getImageName(self):
		return self.imageFileName
	
	def setImageName(self,name):
		self.imageFileName = name
		self.loadImage()
	
	def loadImage(self):
		fn = os.path.join(IMAGEDIR,self.imageFileName)
		print "Media: loading image",fn
		self.srcImage = load(fn)
		print "-- Media loaded:",self.srcImage
			
	def getImage(self,facing=N):
		if self.srcImage is not None and self.rotations[facing] is None:
			img = scale(self.srcImage,(OSIZE_V,OSIZE_V))
			if facing != N:
				deg = 0
				if facing == NW:
					deg = 45
				elif facing == W:
					deg = 90
				elif facing == SW:
					deg = 135
				elif facing == S:
					deg = 180
				elif facing == SE:
					deg = -135
				elif facing == E:
					deg = -90
				elif facing == NE:
					deg = -45
				img = rotate(img,deg)
			self.rotations[facing] = img
		return self.rotations[facing]
