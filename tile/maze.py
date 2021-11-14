#!/usr/bin/python

from collections import defaultdict

L = 1
R = 2
O = 3

BASECOLOR = 0

maze = [
	[O,O,O,O,O,O,O,O],
	[O,R,L,L,R,R,L,O],
	[O,R,L,L,L,R,R,O],
	[O,L,L,R,R,L,R,O],
	[O,R,L,R,L,L,L,O],
	[O,O,O,O,O,O,O,O]
]

colors = {}
curColor = BASECOLOR

def replaceColors(a,b):
	if a == b:
		return
	
	a1 = min(a,b)
	b1 = max(a,b)

	for c in colors:
		x,y,l = colors[c]
		if x == b1:
			x = a1
		if y == b1:
			y = a1
		colors[c] = (x,y,l)

for y in range(len(maze)):
	for x in range(len(maze[y])):
		seg = maze[y][x]
		if seg == O:
			colors[(y,x)] = (BASECOLOR,BASECOLOR,O)
			if x > 0:
				replaceColors(BASECOLOR,colors[(y,x-1)][1])
			if y > 0:
				a,b,l = colors[(y-1,x)]
				if l == L:
					replaceColors(BASECOLOR,b)
				else:
					replaceColors(BASECOLOR,a)
		elif seg == L:
			lc1p = colors[(y-1,x)]
			lc2p = colors[(y,x-1)]
			if lc1p[2] == O:
				lc1 = BASECOLOR
			elif lc1p[2] == L:
				lc1 = lc1p[1]
			else:
				lc1 = lc1p[0]
			lc2 = lc2p[1]
			replaceColors(lc1,lc2)
			curColor += 1
			colors[(y,x)] = (min(lc1,lc2),curColor,L)
		else:
			lc2p = colors[(y-1,x)]
			lc1p = colors[(y,x-1)]
			lc1 = lc1p[1]
			if lc2p[2] == L:
				lc2 = lc2p[1]
			else:
				lc2 = lc2p[0]
			colors[(y,x)] = (lc1,lc2,R)

colorCount = defaultdict(float)
maxArea = 0

for c in colors:
	a,b,l = colors[c]
	if a != BASECOLOR:
		colorCount[a] += 0.5
		maxArea = max(colorCount[a],maxArea)
	if b != BASECOLOR:
		colorCount[b] += 0.5
		maxArea = max(colorCount[b],maxArea)

print "Number of closed areas:",len(colorCount)
print "Largest area",maxArea


