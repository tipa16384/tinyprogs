#!/usr/bin/pythin

red = [ 8, 14, 16, 26, 33, 21 ]
blue = [ 13, 8, 7, 18, 22, 28, 24, 24, 24 ]
green = [11, 9, 8, 16, 14, 16, 27, 39, 42 ]

for r in red:
	for b in blue:
		for g in green:
			if r+b+g == 100:
				print "{} {} {}".format(g,b,r)
