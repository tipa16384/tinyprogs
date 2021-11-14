#!/usr/bin/python

import sys
from random import choice
from time import time

# time to make a move in seconds
moveTime = 0.1

empty = ' '
X = 'X'
O = 'O'
draw = '-'
	
winCheck = [(0,1), (0,3), (0,4), (1,3), (2,2), (2,3), (3,1), (6,1) ]

# clear the board
def clearBoard():
	board = []
	for x in range(9):
		board.append(empty)
	return board

# return who won -- empty if nobody has won
def whoWon(board):
	for start, offset in winCheck:
		play = board[start]
		if play is empty:
			continue
		if board[start+offset] is not play:
			continue
		if board[start+2*offset] is not play:
			continue
		return play
	if not getMoves(board):
		return draw
	return empty

# return possible moves
def getMoves(board):
	moves = [x for x in range(9) if board[x] is empty]
	return moves
	
# print the board
def printBoard(board):
	print "{}|{}|{}   0|1|2".format(board[0], board[1], board[2])
	print "-+-+-   -+-+-"
	print "{}|{}|{}   3|4|5".format(board[3], board[4], board[5])
	print "-+-+-   -+-+-"
	print "{}|{}|{}   6|7|8".format(board[6], board[7], board[8])

	winner = whoWon(board)
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
	board = list(board)
	board[move] = player
	winner = whoWon(board)
	if winner is not empty:
		return winner
	return deepDive(board,nextPlayer(player),choice(getMoves(board)))

board = clearBoard()

player = X

while whoWon(board) is empty:
	startTime = time()
	moves = getMoves(board)
	rankings = {}
	for m in moves:
		rankings[m] = {X:0, O:0, draw:0}
	while (time() - startTime) < moveTime:
		m = choice(moves)
		w = deepDive(board,player,m)
		rankings[m][w] = rankings[m][w] + 1
	print rankings
	ratings = [(x,y[nextPlayer(player)]) for x,y in rankings.items()]
	print ratings
	move = sorted(ratings, key=lambda y:y[1])[0]
	print move
	board[move[0]] = player
	player = nextPlayer(player)
	printBoard(board)
