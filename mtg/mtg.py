#!/usr/bin/python

import json
from random import randint, choice, shuffle
from card import Card

"""Build a deck for me."""

cardlink = 'https://mtgjson.com/json/AllCards.json'

# as of July 19, 2019
cardfile = 'AllCards.json'

commandername = 'Zegana, Utopian Speaker'
commander = None
cardslib = None

mycards = [
	'Armored Wolf-Rider',
	'Sumala Woodshaper',
	'Raven\'s Run Dragoon',
	'Thornbow Archer',
	'Deadbridge Shaman',
	'Eyeblight Assassin',
	'Wildheart Invoker',
	'Nath\'s Elite',
	'Llanowar Empath',
	'Elvish Pathcutter',
	'Symbiotic Elf',
	'Wirewood Elf',
	'Viridian Betrayers',
	'Elvish Warrior',
	'Silhana Starfletcher',
	'Ground Assault',
	'Savage Smash',
	'Branching Bolt',
	'Gruul War Chant',
	'Join Shields',
	'Sundering Growth',
	'Flower',
	'Flourish',
	'Pit Fight',
	'Worldsoul Colossus',
	'Streetbreaker Wurm',
	'Ruination Wurm',
	'Nacatl Outlander',
	'Mudbrawler Raiders',
	'Sunder Shaman',
	'Rubble Slinger',
	'Rubblebelt Runner',
	'Zhur-Taa Druid',
	'Bronzebeak Moa',
	'Scuzzback Marauders',
	'Overgrown Tomb',
	'Cast Down',
	'Seekers\' Squire',
	'Wildgrowth Walker',
	'Golgari Guildgate',
	'Woodland Cemetery',
	'Ravenous Chupacabra',
	'Murder',
	'The Eldest Reborn',
	'Find',
	'Finality',
	'Merfolk Branchwalker',
	'Golgari Findbroker',
	'District Guide',
	'Llanowar Elves',
	'Memorial to Folly',
	'Plaguecrafter',
	'Jadelight Ranger',
	'Vraska, Relic Seeker',
	'Kraul Harpooner',
	'Reclamation Sage',
	'Golden Demise',
	'Duress',
	'Arguel\'s Blood Fast',
	'Gyre Sage',
	'Vinelasher Kudzu',
	'Vorel of the Hull Clade',
	'Zegana, Utopian Speaker',
	'Cytoplast Root-Kin',
	'Fathom Mage',
	'Omnibian',
	'Momir Vig, Simic Visionary',
	'Progenitor Mimic',
	'Experiment Kraj',
	'Simic Sky Swallower',
	'Simic Ascendancy',
	'Voidslime',
	'Guardian Project',
	'Experiment One',
	'Cloudfin Raptor',
	'Coiling Oracle',
	'Zameck Guildmage',
	'Elusive Krasis',
	'Plaxcaster Frogling',
	'Trygon Predator',
	'Skitter Eel',
	'Frilled Mystic',
	'Trollbred Guardian',
	'Galloping Lizrog',
	'Nimbus Swimmer',
	'Simic Guildgate',
	'Simic Growth Chamber',
	'Rapid Hybridization',
	'Simic Signet',
	'Applied Biomancy',
	'Miming Slime',
	'Urban Evolution',
	'Bident of Thassa',
	'Crushing Canopy',
	'Devkarin Dissident',
	'Plummet',
	'Affectionate Indrik',
	'Titanic Growth',
	'Oakenform',
	'Rabid Bite',
	'Sumala Woodshaper',
	'Pause for Reflection',
	'Prey Upon',
	'Vernadi Shieldmate',
	'Kraul Foragers',
	'Chainer\'s Torment',
	'Hydroid Krasis',
	'Sauroform Hybrid',
	'Chillbringer',
	'Simic Locket',
	'Sphinx of the Guildpact',
	'Combine Guildmage',
	'Wilderness Reclamation',
	'Steeple Creeper',
	'Faerie Duelist',
	'Clear the Mind',
	'Territorial Boar',
	'Growth Spiral'
]

alwaysArriveTapped = [
	'Simic Guildgate'
]

def readcards(fn):
	global cardslib
	print 'Reading cards...'
	cards = []
	with open(fn, 'r') as f:
		contents = f.read()
		cardslib = json.loads(contents)
		for c in cardslib:
			cards.append(Card(cardslib[c]))
		print '{} cards read'.format(len(cards))
	return cards

def findCard(cardname):
	if cardname in cardslib:
		return Card(cardslib[cardname])
	return None

def removeFromCollection(collection, card):
	return [x for x in collection if x.name() != card.name()]

def verifycards(cards, cardnames):
	global commander
	
	print cards[0]
	found = [x for x in cards if x.name() in cardnames]
	unfound = [x for x in cardnames if findCard(x) is None]
	print "verified: {}/{}".format(len(found), len(cardnames))
	print "unverified: {}/{}".format(len(unfound), len(cardnames))
	
	if len(unfound):
		for x in unfound:
			print "not found: {}".format(x)

	legal = [x for x in found if x.isLegal()]
	print "legal: {}/{}".format(len(legal), len(cardnames))
	
	commander = findCard(commandername)
	if not commander:
		return None
		
	legal = removeFromCollection(legal, commander)
	
	print "Recruited commander. Reviewing the troops."
	troops = []
	
	for troop in legal:
		print 'troop', troop, troop.colorIdentity()
		badcolors = False
		for color in troop.colorIdentity():
			if color not in commander.colorIdentity():
				badcolors = True
				break
		if not badcolors:
			troops.append(troop)
	
	print "Cards matching commander colors: {}".format(len(troops))
	
	return troops

def constructlands(cards, deck, targetsize):
	colorpool = []
	for card in deck:
		for color in card.colors():
			colorpool.append(color)
	while len(deck) < targetsize:
		color = choice(colorpool)
		if color == u'W':
			deck.append(findCard('Plains'))
		elif color == u'B':
			deck.append(findCard('Swamp'))
		elif color == u'G':
			deck.append(findCard('Forest'))
		elif color == u'U':
			deck.append(findCard('Island'))
		elif color == u'R':
			deck.append(findCard('Mountain'))

def printdeck(deck):
	print ', '.join(x.name() for x in deck)

def draw(hand, library):
	print "---> draw"
	try:
		card = library.pop()
		hand.append(card)
		card.untap()
		print "I drew {}".format(card.name())
	except IndexError, e:
		print "error",e
		pass

def isCardOnBattlefield(battlefield, *names):
	for card in battlefield:
		if card.name() in names:
			return True
	return False

def placeOnBattlefield(battlefield, card):
	tapMe = False
	if card.name() == 'Woodland Cemetary' and not isCardOnBattlefield(battlefield, 'Forest', 'Swamp'):
		tapMe = True
	if card.name() in alwaysArriveTapped:
		tapMe = True
	if tapMe:
		card.tap()
		print 'It comes in tapped.'
	else:
		card.untap()
	battlefield.append(card)
	print "Placed on battlefield: {}".format(card.name())

def untapphase(hand, library, battlefield, graveyard, exile, commandzone):
	print "---> untap"
	for card in battlefield:
		if card.tapped():
			card.untap()
			print "Untapped {}".format(card.name())

def playland(hand, library, battlefield, graveyard, exile, commandzone):
	print "---> play a land"
	lands = [x for x in hand if x.isLand()]
	print "---> {} lands in hand".format(len(lands))
	if lands:
		land = choice(lands)
		hand.remove(land)
		print 'I choose a land: {}'.format(land.name())
		placeOnBattlefield(battlefield, land)

def discard(hand, graveyard):
	while len(hand) > 7:
		card = choice(hand)
		hand.remove(card)
		graveyard.append(card)
		print "Discarded {}".format(card.name())

def hasMana(battlefield, card):
	action = card.findMana()
	if action:
		print "Action {} {}".format(card, action)
	return ([], card)
		
def spellcasting(hand, library, battlefield, graveyard, exile, commandzone):
	print "---> cast a spell"
	castable = [hasMana(battlefield, x) for x in hand if not x.isLand() and hasMana(battlefield,x)[0]]
	num = len(castable)
	print "Number castable cards {}".format(num)
	return num > 0

def play(library):
	# initial hand
	hand = []
	battlefield = []
	exile = []
	graveyard = []
	commandzone = [commander]
	turncount = 0
	
	for i in range(0,7):
		draw(hand, library)
	print "Starting Hand"
	printdeck(hand)
	while library and turncount < 10:
		turncount += 1
		print '---------------------------------------------------------'
		print "Beginning of turn {}".format(turncount)
		printdeck(hand)
		untapphase(hand, library, battlefield, graveyard, exile, commandzone)
		draw(hand, library)
		# play a land
		playland(hand, library, battlefield, graveyard, exile, commandzone)
		# cast a spell
		while spellcasting(hand, library, battlefield, graveyard, exile, commandzone):
			pass
		# discard down to seven
		discard(hand, graveyard)

def findwolves(cards):
	for card in cards:
		if card.isWolf():
			print '1x {}'.format(card.name())

def hasMana(cards):
	for card in cards:
		if card.tapsForMana():
			print '{}'.format(card.name())

def notElves(cards):
	for card in cards:
		if card.giveGreen():
			print '{}'.format(card.name())


			
cards = readcards(cardfile)
notElves(cards)
#deck = verifycards(cards, mycards)
#constructlands(cards, deck, 99)

#shuffle(deck)
#play(deck)

