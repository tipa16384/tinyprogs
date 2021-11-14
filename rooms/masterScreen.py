# masterScreen.py

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
from gamescreen import GameScreen

from screen import Screen
from controlScreen import ControlScreen

class MasterScreen:
	def __init__(self):
		pygame.init()

	def initScreen(self):
		self.masterScreen = pygame.display.set_mode((SCREENW,SCREENH))
		self.subScreens = []
		self.mapScreen = Screen(self.masterScreen,Rect(CONTROLSW,0,PORTW,PORTH))
		self.subScreens.append(self.mapScreen)
		self.subScreens.append(ControlScreen(self.masterScreen,Rect(0,0,CONTROLSW,PORTH)))
		pygame.display.flip()

	def setPlayer(self,player):
		self.mapScreen.setPlayer(player)
		self.mapScreen.setMonsters()

	def setBoard(self,board):
		for gs in self.subScreens:
			gs.setBoard(board)

	def click(self,button,pos):
		for gs in self.subScreens:
			offs = gs.get_offset()
			size = gs.get_size()
			npos = (pos[0]-offs[0],pos[1]-offs[1])
			if npos[0] >= 0 and npos[1] >= 0 and npos[0] < size[0] and npos[1] < size[1]:
				gs.click(button,npos)

	def keystroke(self,key):
		for gs in self.subScreens:
			gs.keystroke(key)

	def draw(self):
		self.masterScreen.fill(Color('white'))
		for gs in self.subScreens:
			gs.draw()
		pygame.display.flip()
