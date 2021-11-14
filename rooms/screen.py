# screen.py

from gamevars import *
import pygame
import pygame.time
from pygame.locals import *
from pygame.sprite import *
import pygame.event
from pygame import Rect
from random import randint
from monster import generateMonsters
from otarget import Target

class Screen:
	def __init__(self):
		print "initializing screen"
		pygame.init()
		self.mobs = LayeredDirty()
		self.scrollPos = (0,0)
		self.player = None
		
	def setMonsters(self):
		generateMonsters(self.mobs)
		
	def setPlayer(self,p):
		self.mobs.add(p,layer=p.getType())
		self.player = p
		self.target = Target()
		self.mobs.add(self.target,layer=self.target.getType())
			
		print "player pos",p.pos

	def initScreen(self):
		self.screen = pygame.display.set_mode((SCREENW,SCREENH))
		self.chroma = pygame.Color(BGCOLOR)
		self.graphColor = pygame.Color(0,200,255,75)
		self.borderColor = pygame.Color("black")
		self.doorColor = pygame.Color("red")
		self.grayColor = pygame.Color(200,200,200)
		self.visitedFloorColor = {}
		self.screen.fill(self.chroma)
		pygame.display.flip()

	def moveMobs(self,board):
		for g in self.mobs:
			if g.getType() == O_MONSTER:
				g.doSomething(board,self.player,self.mobs)
	
	def scroll(self):
		p = self.player
		sw = self.scrollPos[0]
		sh = self.scrollPos[1]
		
		if p is not None:
			if (p.pos[0]-sw) < POSLAG:
				sw = p.pos[0] - POSLAG
			if (sw+PORTSIZE[0]-p.pos[0]) < POSLAG:
				sw = p.pos[0]+POSLAG-PORTSIZE[0]
			if (p.pos[1]-sh) < POSLAG:
				sh = p.pos[1] - POSLAG
			if (sh+PORTSIZE[1]-p.pos[1]) < POSLAG:
				sh = p.pos[1]+POSLAG-PORTSIZE[1]
			if sw < 0:
				sw = 0
			if sw+PORTSIZE[0] > ROOMW:
				sw = ROOMW - PORTSIZE[0]
			if sh < 0:
				sh = 0
			if sh+PORTSIZE[1] > ROOMH:
				sh = ROOMH - PORTSIZE[1]

		self.scrollPos = (sw,sh)
		
	def updateObjects(self,board,grp):
		#print "updating group",g
		
		self.target.visible = 0
		for g in grp:
			if g.targeted:
				self.target.visible = 1
				self.target.setPos(g.getPos())
				break
		
		grp.update(self.scrollPos,board,self.player)
		grp.draw(self.screen)
	
	def drawBG(self,board):
		self.screen.fill(self.chroma)
		ppos = self.player.getPos()
		psym = board.getAt(ppos[0],ppos[1]).getCode()
	
		board.setSeen(psym)
	
		self.drawDeadRooms(board,psym)
	
		self.drawRooms(board,psym,False)

		osize = OSIZE/2
		
		for x in range(osize,SCREENW,osize):
			pygame.draw.line(self.screen,self.graphColor,(x,0),(x,SCREENH))
	
		for y in range(osize,SCREENH,osize):
			pygame.draw.line(self.screen,self.graphColor,(0,y),(SCREENW,y))
	
		self.drawRooms(board,psym,True)
	
	def drawDeadRooms(self,board,xsym):
		for x in range(self.scrollPos[0],self.scrollPos[0]+PORTSIZE[0]):
			for y in range(self.scrollPos[1],self.scrollPos[1]+PORTSIZE[1]):
				spot = board.getAt(x,y)
				if not spot.isRoom() or spot.getCode() == xsym or not board.isSeen(spot.getCode()):
					continue
				rx = (x-self.scrollPos[0]) * OSIZE
				ry = (y-self.scrollPos[1]) * OSIZE
				if spot.getCode() not in self.visitedFloorColor:
					self.visitedFloorColor[spot.getCode()] = pygame.Color(randint(230,250),randint(230,250),randint(230,250))
				self.screen.fill(self.visitedFloorColor[spot.getCode()],Rect(rx,ry,OSIZE,OSIZE))
				
	def drawRooms(self,board,xsym,show):
		for x in range(self.scrollPos[0],self.scrollPos[0]+PORTSIZE[0]):
			for y in range(self.scrollPos[1],self.scrollPos[1]+PORTSIZE[1]):
				spot = board.getAt(x,y)

				if not show:
					if not spot.isRoom():
						continue
					psym = spot.getCode()
					if not board.isSeen(psym):
						continue
				elif spot.getCode() != xsym:
					continue
				else:
					psym = xsym
					
				if spot.getCode() == psym:
					rx = (x-self.scrollPos[0]) * OSIZE
					ry = (y-self.scrollPos[1]) * OSIZE
					spot = board.getAt(x-1,y)
					if spot.getCode() != psym:
						color = show and self.borderColor or self.grayColor
						if spot.look(E) is not None:
							#print "door w"
							color = self.doorColor
						r = Rect(rx-BSIZE/2,ry,BSIZE,OSIZE)
						if not show:
							color = self.grayColor
						self.screen.fill(color,r)
						pygame.draw.circle(self.screen,color,(rx,ry),BSIZE/2)
						pygame.draw.circle(self.screen,color,(rx,ry+OSIZE),BSIZE/2)
					spot = board.getAt(x+1,y)
					if spot.getCode() != psym:
						color = self.borderColor
						if spot.look(W) is not None:
							#print "door e"
							color = self.doorColor
						if not show:
							color = self.grayColor
						r = Rect(rx+OSIZE-BSIZE/2,ry,BSIZE,OSIZE)
						self.screen.fill(color,r)
						pygame.draw.circle(self.screen,color,(rx+OSIZE,ry),BSIZE/2)
						pygame.draw.circle(self.screen,color,(rx+OSIZE,ry+OSIZE),BSIZE/2)
					spot = board.getAt(x,y-1)
					if spot.getCode() != psym:
						color = self.borderColor
						if spot.look(S) is not None:
							#print "door n"
							color = self.doorColor
						if not show:
							color = self.grayColor
						r = Rect(rx,ry-BSIZE/2,OSIZE,BSIZE)
						self.screen.fill(color,r)
						pygame.draw.circle(self.screen,color,(rx,ry),BSIZE/2)
						pygame.draw.circle(self.screen,color,(rx+OSIZE,ry),BSIZE/2)
					spot = board.getAt(x,y+1)
					if spot.getCode() != psym:
						color = self.borderColor
						if spot.look(N) is not None:
							#print "door s"
							color = self.doorColor
						if not show:
							color = self.grayColor
						r = Rect(rx,ry+OSIZE-BSIZE/2,OSIZE,BSIZE)
						self.screen.fill(color,r)
						pygame.draw.circle(self.screen,color,(rx,ry+OSIZE),BSIZE/2)
						pygame.draw.circle(self.screen,color,(rx+OSIZE,ry+OSIZE),BSIZE/2)
	
	def click(self,button,pos):
		x = pos[0]/OSIZE + self.scrollPos[0]
		y = pos[1]/OSIZE + self.scrollPos[1]
		print "clicked",x,y
		gpos = (x,y)
		targeted = None
		
		for g in self.mobs:
			if g.getPos() == gpos and g.getType() > O_TARGET:
				g.targeted = True
				targeted = g
			else:
				g.targeted = False
	
		print "current target",targeted
			
	def updateScreen(self,board):
		self.scroll()
		self.drawBG(board)
		self.updateObjects(board,self.mobs)
		pygame.display.flip()
		