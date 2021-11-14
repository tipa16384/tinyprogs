# globals.py

# filenames

IMAGEDIR = 'images'
PLAYERFN = 'player-top.png'

WALL = '@'
EMPTY = ' '
BASE = 'a'
FLOOR = '.'

ROOMW = 20
ROOMH = 20
NROOMS = 10
NMONSTERS = 5

N = -ROOMW
E = 1
S = ROOMW
W = -1
NW = -ROOMW-1
NE = -ROOMW+1
SW = ROOMW-1
SE = ROOMW+1

ALLDIRS = [N,E,W,S,NE,NW,SE,SW]

BGCOLOR = "white"

OSIZE = 32
OSIZE_V = (OSIZE*10)/8

BSIZE = 6		# should be even
OSPEED = 60

PORTSIZE = (20,15)

SCREENW = PORTSIZE[0]*OSIZE
SCREENH = PORTSIZE[1]*OSIZE
POSLAG = 3

# Monster moods
# Hostile monsters track the player

M_DOCILE = 0
M_HOSTILE = 1

# Monster state

S_NORMAL = 0
S_SLEEPING = 1
S_EXPLORING = 2

# object types (also used for layer)

O_GENERIC = 10
O_MONSTER = 99
O_PLAYER = 100
O_TARGET = 0 # this or any lower layer cannot be targeted.

