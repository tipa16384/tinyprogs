#!/usr/bin/python

import itertools
from math import sqrt
from random import shuffle, sample, choice

payout = { 6:10000,
	7:36,
	8:720,
	9:360,
	10:80,
	11:252,
	12:108,
	13:72,
	14:54,
	15:180,
	16:72,
	17:180,
	18:119,
	19:36,
	20:306,
	21:1080,
	22:144,
	23:1800,
	24:2600}

scoring = [
	(1,2,3),
	(4,5,6),
	(7,8,9),
	(1,4,7),
	(2,5,8),
	(3,6,9),
	(1,5,9),
	(3,5,7)
]
	
# positions are:
# 1 2 3
# 4 5 6
# 7 8 9
# four will be shown

posix = {
	3: 9,
	4: 7,
	7: 8,
	9: 2
}

def rankPosition(position):
	freePositions = range(1,10)
	freeNumbers = range(1,10)

	#print "Setting up"

	for p in position:
		freePositions.remove(p)
		freeNumbers.remove(position[p])

	#print "Permuting"

	topScore = 0
	topPlay = None

	cumScore = {}
	for x in scoring:
		cumScore[x] = []

	for p in itertools.permutations(freeNumbers):
		board = position.copy()
		
		for i in range(len(p)):
			board[freePositions[i]] = p[i]
		
		for x in scoring:
			sc = payout[sum([board[y] for y in x])]
			cumScore[x].append(sc)
			
			if sc > topScore:
				topScore = sc
				topPlay = x

	#print "topPlay", topPlay
	#print "topScore", topScore

	#for k in cumScore:
	#	mean = sum(cumScore[k])/len(cumScore[k])
	#	var = sum([(x-mean)**2 for x in cumScore[k]])/len(cumScore[k])
	#	print k,mean,sqrt(var)
	
	return topPlay

# Expected winnings ~1151
def randomPick():
	board = range(1,10)
	shuffle(board)
	#print "Board", board
	position = {}
	shown = sample(range(1,10),4)
	#print "Shown", shown
	for y in shown:
		position[y] = board[y-1]
	#print "Position ", position
	play = rankPosition(position)
	#print "Play", play, "Board", board
	sm = sum([board[p-1] for p in play])
	#print sm
	return payout[sm]

# Expected winnings ~1286
def huntPick():
	board = range(1,10)
	shuffle(board)
	#print "Board", board
	position = {}
	unused = range(9)
	op = choice(unused)
	unused.remove(op)
	position[op+1] = board[op]
	#print "position",position
	
	for i in range(2,5):
		#print "Move",i
		#print "Current position", position
		hasTarget = reduce(lambda x,y: x or (y<=3), position.values(), False)
		#print "Target found",hasTarget
		if not hasTarget:
			#print "No target random choice"
			op = choice(unused)
			unused.remove(op)
			position[op+1] = board[op]
		else:
			#print "Hunting"
			pots = [s for s in scoring]
			for k in position:
				v = position[k]
				#print "Culling",k,v
				if v <= 3:
					for pot in scoring:
						if pot in pots and k not in pot:
							pots.remove(pot)
				else:
					for pot in scoring:
						if pot in pots and k in pot:
							pots.remove(pot)
			if len(pots) == 0:
				op = choice(unused)
				unused.remove(op)
				position[op+1] = board[op]
			else:
				shuffle(pots)
				mov = pots[0]
				moved = False
				for x in mov:
					op = x - 1
					if x not in position and op in unused:
						position[x] = board[op]
						unused.remove(op)
						moved = True
						break
				if not moved:
					op = choice(unused)
					unused.remove(op)
					position[op+1] = board[op]
					
	#print "Position ", position
	play = rankPosition(position)
	#print "Play", play, "Board", board
	sm = sum([board[p-1] for p in play])
	#print sm, payout[sm]
	return payout[sm]
				
	
	
winnings = 0
tries = 50000

#huntPick()

#for x in range(tries):
#	winnings += randomPick()

#print "Average ", (winnings/tries)

print rankPosition(posix)
