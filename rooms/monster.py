# monster.py

from gamevars import *
import pygame
import pygame.time
from pygame.locals import *
from pygame.sprite import *
import pygame.event
from pygame import Rect
from random import randint, choice, shuffle

from object import Object

def generateMonsters(group):
	for x in range(NMONSTERS):
		placed = False
		while not placed:
			pos = (randint(1,ROOMW-2),randint(1,ROOMH-2))
			placed = True
			for o in group:
				if o.getPos() == pos:
					placed = False
					break
			if placed:
				m = Monster()
				m.setDesc('Dire Rat')
				m.setLDesc('a dire rat')
				m.setType(O_MONSTER)
				m.setImageName('rat-top.png')
				m.setPos(pos)
				group.add(m,layer=m.getType())

class Monster(Object):
	def __init__(self):
		Object.__init__(self)
		self.setDesc('Monster')
		self.setLDesc('a monster')
		self.setType(O_MONSTER)
		self.speed = OSPEED
		self.mood = M_DOCILE
		self.state = S_NORMAL
		self.newPos = None
		self.goal = None
		
	def canMove(self,facing,board,group):
		okay = False
		self.newPos = None
		
		dx = 0
		dy = 0
		
		x = self.pos[0]
		y = self.pos[1]

		if facing == N:
			dy = -1
		elif facing == NW:
			dx = -1
			dy = -1
		elif facing == W:
			dx = -1
		elif facing == SW:
			dx = -1
			dy = 1
		elif facing == S:
			dy = 1
		elif facing == SE:
			dy = 1
			dx = 1
		elif facing == E:
			dx = 1
		elif facing == NE:
			dx = 1
			dy = -1
		
		nx = x + dx
		ny = y + dy
		
		if nx < 1:
			nx = 1
		elif nx > ROOMW-2:
			nx = ROOMW-2
		if ny < 1:
			ny = 1
		elif ny > ROOMH-2:
			ny = ROOMH-2
		
		if x != nx or y != ny:
			spot = board.getAt(x,y)
			nspot = board.getAt(nx,ny)
		
			if spot.getCode() == nspot.getCode():
				okay = True
			elif nspot.isRoom():
				if facing == N or facing == E or facing == W or facing == S:
					door = spot.look(facing)
					if door is not None:
						okay = True
		
			npos = (nx,ny)
			
			if okay:
				for mob in group:
					if mob != self and mob.getPos() == npos and mob.getType() != O_GENERIC:
						okay = False
						break
						
			if okay:
				self.newPos = npos

		return okay
	
	def doSomething(self,board,player,group):
		ppos = player.getPos()
		pspot = board.getAt(ppos[0],ppos[1])
		proom = pspot.getCode()
		pos = self.getPos()
		spot = board.getAt(pos[0],pos[1])
		room = spot.getCode()
		
		if proom == room:
			self.mood = M_HOSTILE
		
		choices = []
		dx = 0
		dy = 0
		nch = []
		f = None
		
		if spot.getScent() > 0:
			#print "on the trail",self
			bestSmell = spot.getScent()
			bestFace = None
			for f in ALLDIRS:
				if self.canMove(f,board,group):
					npos = board.getAt(self.newPos[0],self.newPos[1])
					if npos.getScent() > bestSmell:
						bestFace = f
						bestSmell = npos.getScent()
			if bestFace is not None:
				choices = [bestFace]
		else:
			if self.mood == M_HOSTILE:
				dx = ppos[0] - pos[0]
				dy = ppos[1] - pos[1]
			else:
				if self.goal == None or self.goal == pos:
					self.goal = (randint(1,ROOMW-2),randint(1,ROOMH-2))
				dx = self.goal[0] - pos[0]
				dy = self.goal[1] - pos[1]
		
			if dx < 0 and dy < 0:
				f = NW
				nch = [W,N]
			elif dx == 0 and dy < 0:
				f = N
				nch = [NW,NE]
			elif dx > 0 and dy < 0:
				f = NE
				nch = [N,E]
			elif dx < 0 and dy == 0:
				f = W
				nch = [NW,SW]
			elif dx > 0 and dy == 0:
				f = E
				nch = [NE,SE]
			elif dx < 0 and dy > 0:
				f = SW
				nch = [W,S]
			elif dx == 0 and dy > 0:
				f = S
				nch = [SW,SE]
			elif dx > 0 and dy > 0:
				f = SE
				nch = [S,E]
				
			if f is not None:
				if self.canMove(f,board,group):
					choices = [f]
				else:
					for f in nch:
						if self.canMove(f,board,group):
							choices.append(f)
		
		if len(choices) == 0:
			for f in ALLDIRS:
				if self.canMove(f,board,group):
					choices.append(f)

		if len(choices) > 0:
			f = choice(choices)
			if f is not None:
				self.move(f,board,group)

	def move(self,facing,board,group):
		self.setDir(facing)
		okay = self.canMove(facing,board,group)
		if okay:
			self.pos = self.newPos
		return okay
