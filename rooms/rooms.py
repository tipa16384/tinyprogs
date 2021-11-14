#!/usr/bin/python

from board import Board
from screen import Screen
import pygame
import pygame.time
from pygame.locals import *
import pygame.event
from player import Player
from gamevars import *

class Main:
	def __init__(self):
		self.board = Board()
		self.screen = Screen()
		self.userQuit = False
		self.updateBoard = True
		
		self.player = Player()
		self.screen.setPlayer(self.player)
		self.screen.setMonsters()
	
	def initialize(self):
		self.board.setUp()
		self.screen.initScreen()
		
	def printBoard(self):
		self.board.show()

	def processEvents(self):
		e = pygame.event.poll()
		if e is not None:
			if e.type == MOUSEBUTTONDOWN:
				self.screen.click(e.button,e.pos)
				self.updateBoard = True
			elif e.type == KEYDOWN:
				self.updateBoard = True
				moveDir = None
				moveMonsters = False
				if e.key == K_q:
					self.userQuit = True
				elif e.key == K_h:
					moveDir = W
				elif e.key == K_j:
					moveDir = S
				elif e.key == K_k:
					moveDir = N
				elif e.key == K_l:
					moveDir = E
				elif e.key == K_y:
					moveDir = NW
				elif e.key == K_u:
					moveDir = NE
				elif e.key == K_n:
					moveDir = SW
				elif e.key == K_m:
					moveDir = SE
				elif e.key == K_PERIOD:
					moveMonsters = True

				if moveDir != None:
					self.player.move(moveDir,self.board,self.screen.mobs)
					moveMonsters = True
				
				if moveMonsters:
					self.screen.moveMobs(self.board)
	
	def run(self):
		print "running..."
		while not self.userQuit:
			if self.updateBoard:
				self.screen.updateScreen(self.board)
				self.updateBoard = False
			pygame.time.wait(5)
			self.processEvents()

main = Main()
main.initialize()
main.printBoard()

main.run()
