#!/usr/bin/python

from random import random

maxsteps = 100000

couchdist = 0
timeatcouch = 0

for step in range(maxsteps):
	roll = random()
	if couchdist is 0:
		if roll <= 0.25:
			couchdist = 1 
	elif roll <= 0.25:
		couchdist += 1
	elif roll <= 0.75:
		couchdist -= 1 
	if couchdist is 0:
		timeatcouch += 1 

print "After {} steps, baby stayed at couch {}% of the time.".format(maxsteps, float(timeatcouch*100)/float(maxsteps))
