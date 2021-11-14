#!/usr/bin/python

import sys
from random import choice
from time import time
import pyjs

# time to make a move in seconds
moveTime = 15

empty = '.'
X = 'X'
O = 'O'
draw = '-'
wall = '#'

human = X
	
# clear the board
def clearBoard():
	board = []
	for x in range(100):
		board.append(empty)
	
	for x in range(10):
		board[x] = wall
		board[x+90] = wall
		board[10*x] = wall
		board[10*x+9] = wall
	
	board[44] = O
	board[45] = X
	board[54] = X
	board[55] = O
	return board

# return who won -- empty if nobody has won
def whoWon(board,player):
	other = nextPlayer(player)
	
	# someone can still move, so not done yet
	if getMoves(board,player) or getMoves(board,other):
		return empty
	
	#print "possible winner"
	
	score = {player:0, other:0, empty:0, wall:0}
	
	for s in board:
		score[s] = score[s] + 1
	
	# final player counts empty squares
	score[player] = score[player] + score[empty]
	
	# if still a tie, final player wins
	if score[player] >= score[other]:
		return player
	
	# if that wasn't enough, then the other player won.
	return other

# return possible moves
def getMoves(board,player):
	moves = [x for x in range(100) if board[x] is empty and canflip(board,player,x)]
	
	#print "getMoves {}".format(moves)

	return moves

offsets = [1,-1,10,-10,9,11,-9,-11]
	
def canflip(board,player,pos):
	other = nextPlayer(player)
	flipped = []
	for o in offsets:
		posflip = []
		p = pos
		while (p+o) >= 0 and (p+o) < 100 and board[p+o] is other:
			p += o
			posflip.append(p)
		if posflip and (p+o) >= 0 and (p+o) < 100 and board[p+o] is player:
			flipped += posflip
	#print "canflip {} {} {}".format(player,pos,flipped)
	#if not flipped:
	#	print "NO MOVES"
	return flipped
	
# print the board
def printBoard(board,player):
	top = '  01234567'
	
	print top
	for row in range(11,90,10):
		i = (row-1)/10+64
		s = ''.join([board[col] for col in range(row,row+8)])
		print "{} {} {}".format(chr(i),s,chr(i))
	print top
	
	winner = whoWon(board,player)
	if winner is not empty:
		print
		if winner is draw:
			print "The game ends in a draw"
		else:
			print "{} is the winner".format(winner)
	
	print
	
# switch players
def nextPlayer(player):
	if player is X:
		return O
	if player is O:
		return X
	return player

def deepDive(board,player,move):
	other = nextPlayer(player)
	board = list(board)
	makeMove(board,player,move)
	winner = whoWon(board,player)
	if winner is not empty:
		return winner
	
	moves = getMoves(board,other)
	
	if moves:
		return deepDive(board,other,choice(moves))
	
	moves = getMoves(board,player)
	
	return deepDive(board,player,choice(moves))

def makeMove(board,player,move):
	flipped = canflip(board,player,move)
	
	if len(flipped) == 0:
		print "{} is not a legal move for {}".format(move,player)
		sys.exit(1)
	
	#printBoard(board,player)
	for p in flipped:
		board[p] = player
	board[move] = player
	#printBoard(board,player)
	#print "moved player {} to {} and flipped {}".format(player,move,flipped)

def cpuMove(board,player,moves):
	startTime = time()
	rankings = {}
	for m in moves:
		rankings[m] = {X:0, O:0, draw:0}
	while (time() - startTime) < moveTime:
		m = choice(moves)
		w = deepDive(board,player,m)
		rankings[m][w] = rankings[m][w] + 1
	#print rankings
	ratings = [(x,y[player],y[other]) for x,y in rankings.items()]
	#print ratings
	move = sorted(ratings, key=lambda y:y[1], reverse=True)[0]
	print "{} moves to {}".format(player,indexToMove(move[0]))
	print "{} is winning".format(player if move[1] > move[2] else other)
	return move[0]

def indexToMove(idx):
	row = chr(64+idx/10)
	col = chr(47+idx%10)
	return "{}{}".format(row,col)

def humanMove(moves):
	legalMoves = [indexToMove(m) for m in moves]
	
	while(True):
		m = raw_input('Your move: ').strip().upper()
		if m in legalMoves:
			break
		print "Move must be in {}".format(', '.join(legalMoves))
	
	row = ord(m[0])-64
	col = ord(m[1])-47
	
	m = row*10 + col
	print "Move was: {}".format(indexToMove(m))
	return m
	
board = clearBoard()

player = X

printBoard(board,player)

while whoWon(board,player) is empty:
	other = nextPlayer(player)
	
	moves = getMoves(board,player)
	print "Possible moves: {}".format(', '.join([indexToMove(m) for m in moves]))
	
	if moves:
		if player is human:
			m = humanMove(moves)
		else:
			m = cpuMove(board,player,moves)
		makeMove(board,player,m)
	else:
		print "{} passes".format(player)
		
	printBoard(board,player)
	player = other
