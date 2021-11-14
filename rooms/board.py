from random import randint, choice, shuffle
from spot import Spot
from door import Door
from gamevars import *


class Board:
	def __init__(self):
		self.newArr()
		self.seen = {}
		
	def setUp(self):
		self.initialize()
		self.generate()
		self.connectRooms()
		self.outlineWalls()
	def newArr(self):
		self.arr = [Spot(x) for x in range(ROOMW*ROOMH)]
		for y in range(1,ROOMH-1):
			for x in range(1,ROOMW-1):
				self.setAt(x,y,EMPTY)
	def setAt(self,x,y,code):
		self.getAt(x,y).setCode(code)
	def getAt(self,x,y):
		return self.arr[y*ROOMW+x]
	def getAtExtreme(self,arr,x,y):
		return arr[y*ROOMW+x]
	def getAll(self):
		return self.arr
	def show(self):
		for y in range(ROOMH):
			print ''.join([str(self.getAt(x,y)) for x in range(ROOMW)])
	def neighbors(self,oarr,x,y):
		arr = []
		self.addNeighbor(arr,oarr,x-1,y)
		self.addNeighbor(arr,oarr,x+1,y)
		self.addNeighbor(arr,oarr,x,y-1)
		self.addNeighbor(arr,oarr,x,y+1)
		return arr
	def addNeighbor(self,arr,oarr,x,y):
		sym = self.getAtExtreme(oarr,x,y)
		if sym.isRoom():
			arr.append(sym.getCode())
	
	def isSeen(self,code):
		try:
			return self.seen[code]
		except KeyError:
			return False
	
	def setSeen(self,code):
		self.seen[code] = True
	
	def initialize(self):
		"initializing"
		for r in range(NROOMS):
			sym = chr(ord(BASE)+r)
			occupied = True
			while occupied:
				occupied = False
				w = randint(3,6)
				h = randint(3,6)
				x = randint(1,ROOMW-w-1)
				y = randint(1,ROOMH-h-1)

				for iy in range(y,y+h):
					for ix in range(x,x+w):
						if self.getAt(ix,iy).isRoom():
							occupied = True
							break
					if occupied:
						break
				
				if occupied:
					continue
					
				for iy in range(y,y+h):
					for ix in range(x,x+w):
						self.setAt(ix,iy,sym)

	def allConnected(self,connected):
		goodToGo = True
		for v in connected.values():
			goodToGo = goodToGo and v
		return goodToGo

	def generate(self):
		"generating board (%dx%d)" % (ROOMW,ROOMH)
		changes	=	True
		while	changes:
			changes	=	False
			oldArr = self.arr
			self.newArr()
			for	iy in	range(1,ROOMH-1):
				for	ix in	range(1,ROOMW-1):
					sym	=	self.getAtExtreme(oldArr,ix,iy)
					if sym.isRoom():
						self.setAt(ix,iy,sym.getCode())
					elif sym.getCode() ==	EMPTY:
						arr	=	self.neighbors(oldArr,ix,iy)
						if len(arr)	>	0:
							sym	=	choice(arr)
							self.setAt(ix,iy,sym)
							changes	=	True

	def connectRooms(self):
		"adding room connectivity"
		
		connectivity = [x for x in range(ROOMW*ROOMH)]
		shuffle(connectivity)
		spaces = self.getAll()
		connected = {}
		
		# no rooms are connected
		
		for s in spaces:
			if s.isRoom():
				connected[s.getCode()] = False
		
		# well, the first room we encounter is
		
		for i in connectivity:
			if spaces[i].isRoom():
				connected[spaces[i].getCode()] = True
				break
		
		while not self.allConnected(connected):
			for i in connectivity:
				s = spaces[i]
				if s.isRoom() and not connected[s.getCode()]:
					neighbors = [N,E,W,S]
					shuffle(neighbors)
					for ni in neighbors:
						n = spaces[ni+i]
						if n.isRoom() and connected[n.getCode()]:
							d = Door()
							s.setDoor(ni,d)
							n.setDoor(-ni,d)
							connected[s.getCode()] = True
							break

	def outlineWalls(self):
		"outlining walls"
		
		spaces = self.getAll()
		
		for i in range(len(spaces)):
			s = spaces[i]
			if not s.isRoom():
				continue
			a = [spaces[i+E],spaces[i+N],spaces[i+W],spaces[i+S],spaces[i+NE],spaces[i+SE],spaces[i+NW],spaces[i+SW]]
			interior = True
			for n in a:
				if n.isRoom() and n.getCode() < s.getCode():
					interior = False
					break
			s.setInterior(interior)
		
