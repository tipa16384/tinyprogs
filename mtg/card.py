#!/usr/bin/python

from random import randint

class Card:
	def __init__(self, jsoncard):
		self.card = jsoncard
		self._tapped = False
		self.id = randint(0,99999999999)
	
	def __str__(self):
		return self.card['name']
	
	def __repr__(self):
		return 'Card(\'{}\')'.format(self.card['name'])
	
	def isLegal(self):
		try:
			return self.card['legalities']['commander'] == 'Legal'
		except:
			return False

	def name(self):
		return self.card['name']
	
	def colorIdentity(self):
		return self.card['colorIdentity']
	
	def colors(self):
		return self.card['colors']
	
	def tap(self):
		self._tapped = True
	
	def untap(self):
		self._tapped = False
	
	def tapped(self):
		return self._tapped

	def types(self):
		return self.card['types']

	def isLand(self):
		return 'Land' in self.types()
	
	def isCreature(self):
		return 'Creature' in self.types()
	
	def findMana(self):
		actions = self.card['text'].split('\n')
		for action in actions:
			if '{T}' in action and 'Add' in action:
				return action
	
	def isWolf(self):
		try:
			woof = 'Wolf' in self.card['type'] or 'Wolf' in self.card['text']
			return woof
		except:
			return False

	def tapsForMana(self):
		try:
			return ('Add {G} or {W}' in self.card['text'] or 'Add {G}{W}' in self.card['text']) and \
				('tapped unless' in self.card['text'] or not 'tapped' in self.card['text'])
		except:
			return False

	def giveGreen(self):
		try:
			return 'Add {G}' in self.card['text'] and self.isCreature() and self.card['convertedManaCost'] == 1.0
		except:
			return False


