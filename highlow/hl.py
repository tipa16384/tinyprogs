#!/usr/bin/python
from random import shuffle

hers = [1,4]
mine = 8
tries = 10000

high = 0
low = 0
draw = 0

deck = range(1,10)

for x in hers:
	deck.remove(x)

deck.remove(mine)

for i in range(tries):
	shuffle(deck)
	hertotal = sum(hers) + deck[0]
	mytotal = mine + deck[1] + deck[2]
	if mytotal > hertotal:
		high += 1
	elif mytotal < hertotal:
		low += 1
	else:
		draw += 1

if high > low:
	print "guess high"
elif low > high:
	print "guess low"
else:
	print "probably a draw."
