# player.py

from gamevars import *
from monster import Monster

class Player(Monster):
	def __init__(self):
		print "player: initializing"
		Monster.__init__(self)
		self.setDesc('Player')
		self.setLDesc('the player')
		self.setType(O_PLAYER)
		self.setImageName(PLAYERFN)
		self.setPos((ROOMW/2,ROOMH/2))
		self.steps = 0
		
		self.setDir(N)

	def move(self,facing,board,group):
		if Monster.move(self,facing,board,group):
			self.steps = self.steps+1
			spot = board.getAt(self.pos[0],self.pos[1])
			spot.setScent(self.steps)

