# 7DRL
# Class for a square of the room

from gamevars import *

class Spot:
	def __init__(self,num):
		self.code = WALL
		self.num = num
		self.dirs = { N:None, E:None, W:None, S:None }
		self.interior = False
		self.scent = 0
	
	# scent is the step # when the player last was in this space.
	# tracking creatures will follow the scent to find the player
	# by following spaces of increasing scent.
	
	def setScent(self,scent):
		self.scent = scent
	
	def getScent(self):
		return self.scent
		
	def getCode(self):
		return self.code

	def setCode(self,code):
		self.code = code

	def isRoom(self):
		return self.code != WALL and self.code != EMPTY

	def getNumber(self):
		return self.num

	def isInterior(self):
		return self.interior
	
	def setInterior(self,inside):
		self.interior = inside

	def look(self,at):
		try:
			return self.dirs[at]
		except KeyError:
			return None
	
	def setDoor(self,at,door):
		self.dirs[at] = door
		
	def __str__(self):
		for d in self.dirs.values():
			if d is not None:
				return self.code.upper()
		if self.interior:
			return FLOOR
		else:
			return self.code
