#!/usr/bin/python

BW = 10
BH = BW

room = [BW][BH]

for x in range(BW):
    for y in range(BH):
        room[x][y] = '.'

print room[3][4]
