# gamescreen.py

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

class GameScreen:
	def __init__(self,masterScreen,bounds):
		self.screen = masterScreen.subsurface(bounds)
		self.board = None
		
	def draw(self):
		pass
	
	def click(self,button,pos):
		pass

	def keystroke(self,key):
		pass
	
	def setBoard(self,board):
		self.board = board
	
	def getBoard(self):
		return self.board
		