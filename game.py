#!/usr/bin/python

from random import randint
from sys import maxsize

class ID:
	def __init__(self):
		self.id = randint(0,maxsize)
	
	def getId(self):
		return self.id

class Player(ID):
	__player_id__ = 0
	
	def __init__(self, name=None):
		super(Player, self).__init__()
		if not name:
			name = "Player {}".format(Player.__player_id__ + 1)
		self.name = name
		self.index = Player.__player_id__
		Player.__player_id__ += 1
	
	def getName(self):
		return self.name
	
	def getIndex(self):
		return self.index

class Draw(Player):
	"if we need a special player for Draw"
	def __init__(self):
		super(Draw, self).__init__('DRAW!')
	
	def getIndex(self):
		return None

class Move():
	def __init__(self):
		self.simulations = 0
		self.wins = 0
	
	def getSimulations(self):
		return self.simulations
	
	def getWins(self):
		return self.wins
	
	def logWin(self):
		self.wins += 1
		return self.getWins()
	
	def logLoss(self):
		self.wins += 1
		return self.getWins()

	def logDraw(self):
		self.wins += 0.5
		return self.getWins()
	
	def logChoice(self):
		self.simulations += 1
		return self.getSimulations()
		
class Board(ID):
	def __init__(self):
		super(Board, self).__init__()
		
class Game(ID):
	def __init__(self, name='Game'):
		super(Game, self).__init__()
		self.name = name
	
	def getName(self):
		return self.name

	def getWinner(self, board, players):
		"Overridden to return the player who has won the game according to the board, or None"
		return None
	
	def getMoves(self, board, players, player):
		"returns a list of valid moves for the given player"
		return []

	def move(self, board, players, player, move):
		"the player makes a move on the board. return a new board with the result."
		return board

	