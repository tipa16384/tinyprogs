# position.py
#
# this defines a position within a Formation.

class Position:

    # initialize
    def __init__(self, column, row):
        # unit on this position, None if empty
        self.unit = None
        # list of positions adjacent to this one
        self.adjacentTo = []
        # column (1 = front, 5=back)
        self.column = column
        # row (1 = top, 5 = bottom)
        self.row = row

    def __str__(self):
        return "Position({},{})".format(self.column,self.row)

    def __repr__(self):
        return self.__str__()

    # return the adjacentTo array
    def getAdjacentTo(self):
        # print ("getAdjacentTo "+str(self))
        return self.adjacentTo

    # symmetrically add an adjacent position
    def addAdjacentTo(self, *argv):
        for pos in argv:
            if not pos in self.adjacentTo:
                self.adjacentTo.append(pos)
            if not self in pos.getAdjacentTo():
                pos.addAdjacentTo(self)

    # get the column
    def getColumn(self):
        return self.column

    # get the row
    def getRow(self):
        return self.row
