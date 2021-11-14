# Donaar formation

from formation import Formation
from position import Position

donaarFormation = Formation('Donaar')
pos1 = Position(2,2) # top tank
pos2 = Position(2,6) # bottom tank
pos3 = Position(3,1) # top col 2
pos4 = Position(3,3) # middle col 2
pos5 = Position(3,7) # bottom col 2
pos6 = Position(4,2) # top col 3
pos7 = Position(4,4) # middle col 3
pos8 = Position(4,6) # bottom col 3
pos9 = Position(5,1) # top col 5
pos10 = Position(5,7) # bottom col 5
pos1.addAdjacentTo(pos3,pos4)
pos2.addAdjacentTo(pos5)
pos3.addAdjacentTo(pos1,pos4,pos6)
pos4.addAdjacentTo(pos1,pos3,pos6,pos7)
pos5.addAdjacentTo(pos2,pos8)
pos6.addAdjacentTo(pos3,pos4,pos7,pos9)
pos7.addAdjacentTo(pos6,pos4,pos8)
pos8.addAdjacentTo(pos7,pos5,pos10)
pos9.addAdjacentTo(pos6)
pos10.addAdjacentTo(pos8)
donaarFormation.addPosition(pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10)
