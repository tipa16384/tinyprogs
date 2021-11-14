# this defines a formation. it is a map of nodes that have an adjacency to other nodes.f

class Formation:

    # initialization
    def __init__(self, name):
        self._name = name
        self._positions = []
        self._name = []
        self._front = 0
        self._top = 0
        self._bottom = 0
        self._back = 0

    # add a position
    def addPosition(self, *positions):
        for pos in positions:
            self._positions.append(pos)
        self.calc()

    # distance between two positions. For now, all we care about is 1 or 2 away.
    # anything further returns 100 because we just don't care. Yet.
    def distance(self, pos1, pos2):
        if pos2 in pos1.getAdjacentTo():
            return 1
        for pos in pos1.getAdjacentTo():
            if pos2 in pos.getAdjacentTo():
                return 2
        return 100

    # set positional variables
    def calc(self):
        self._front = min([pos.column for pos in self._positions])
        self._back = max([pos.column for pos in self._positions])
        self._top = min([pos.row for pos in self._positions])
        self._bottom = max([pos.row for pos in self._positions])

    # is this position in the front?
    def isFront(self,pos):
        return pos.getColumn() is self._front

    # is this position in the back?
    def isBack(self,pos):
        return pos.getColumn() is self._back

    # is this position on the top?
    def isTop(self,pos):
        return pos.getRow() is self._top

    # return front positions
    def getFront(self):
        return [pos for pos in self._positions if self.isFront(pos)]
