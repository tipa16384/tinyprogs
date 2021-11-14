# Glimmer & Gloom

# dictionary of ten cells and its neighbors
from typing import Tuple
import threading
import time

connections_easy = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E', 'F'],
    'C': ['B', 'F', 'G'],
    'D': ['A', 'E', 'H'],
    'E': ['A', 'B', 'D', 'F', 'H', 'I'],
    'F': ['B', 'C', 'E', 'G', 'I', 'J'],
    'G': ['C', 'F', 'J'],
    'H': ['D', 'E', 'I'],
    'I': ['E', 'F', 'H', 'J'],
    'J': ['F', 'G', 'I']
}

connections_medium = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E', 'F'],
    'C': ['B', 'F', 'G'],
    'D': ['A', 'E', 'H', 'I'],
    'E': ['A', 'B', 'D', 'F', 'I', 'J'],
    'F': ['B', 'C', 'E', 'G', 'J', 'K'],
    'G': ['C', 'F', 'K', 'L'],
    'H': ['D', 'I', 'M'],
    'I': ['D', 'E', 'H', 'J', 'M', 'N'],
    'J': ['E', 'F', 'I', 'K', 'N', 'O'],
    'K': ['F', 'G', 'J', 'L', 'O', 'P'],
    'L': ['G', 'K', 'P'],
    'M': ['H', 'I', 'N', 'Q'],
    'N': ['I', 'J', 'M', 'O', 'Q', 'R'],
    'O': ['J', 'K', 'N', 'P', 'R', 'S'],
    'P': ['K', 'L', 'O', 'S'],
    'Q': ['M', 'N', 'R'],
    'R': ['N', 'O', 'Q', 'S'],
    'S': ['O', 'P', 'R']
}

# dictionary where keys are the keys of connections and the value is False
cells_easy = {
    'A': True,
    'B': False,
    'C': True,
    'D': False,
    'E': False,
    'F': False,
    'G': False,
    'H': True,
    'I': True,
    'J': False
}

# dictionary of letters from A to S set to False
cells_medium = {
    'A': True,
    'B': False,
    'C': False,
    'D': True,
    'E': True,
    'F': True,
    'G': False,
    'H': False,
    'I': True,
    'J': True,
    'K': True,
    'L': False,
    'M': True,
    'N': False,
    'O': True,
    'P': True,
    'Q': True,
    'R': True,
    'S': True
}

cells = cells_medium
connections = connections_medium

state_list = []

# function that takes a cell and flips its polarity and that of its neighbors
def flip(cell, cellsCopy):
    cellsCopy[cell] = not cellsCopy[cell]
    for neighbor in connections[cell]:
        cellsCopy[neighbor] = not cellsCopy[neighbor]

# append the polarities of all the cells as a tuple to the state_list
def save_state(state=None):
    state_list.append(state)

# return true if the state is already in the state_list
def is_repeated(state):
    return state in state_list

# return true if all values in state are True or all values in state are False
def is_stable(state):
    return all(state) or not any(state)
#    return all(state)

# get the state of the cells
def get_state(cellsCopy):
    return tuple(x for x in cellsCopy.values())

solutionDepth = 20
solutions = []

# flip each cell and see if it is stable. If it is, print the sequence of flips. Otherwise, repeat.
def glimmer(cell, depth, flips, tempCells):
    global solutionDepth, solutions
    cellsCopy = tempCells.copy()

    #print(cell, depth, flips)

    flips.append(cell)
    flip(cell, cellsCopy)

    state = get_state(cellsCopy)
    if not is_repeated(state) and depth < solutionDepth:
        #print ('Added state {}'.format(state))

        if not is_stable(state):
            save_state(state)
            for neighbor in cellsCopy:
                glimmer(neighbor, depth + 1, flips, cellsCopy)
        else:
            #print(state, ' '.join(x for x in flips))
            solutionDepth = depth
            solutions.append(flips.copy())
            # print the size of flips
            print("Solution found of size", len(flips), state, flips)
    else:
        time.sleep(0)

    # remove last element of flips
    flips.pop()

# test that two flips of the same cell restore the state to the original
def test_flip(cell):
    cellsCopy = cells.copy()
    state = get_state(cellsCopy)
    flip(cell, cellsCopy)
    flip(cell, cellsCopy)
    return state == get_state(cellsCopy)

def test_glimmer():
    for cell in cells:
        if not test_flip(cell):
            print('Test failed for cell {}'.format(cell))
            return
    print('Test passed')

def run_glimmer():
    
    save_state(get_state(cells))
    for neighbor in cells:
        cellsCopy = cells.copy()
        glimmer(neighbor, 0, [], cellsCopy)
    # print shortest element in solutions
    if solutions:
        # print number of solutions
        print(len(solutions))
        solutions.sort(key=len)
        print (solutions[0])
    else:
        print('No solutions found')

# call glimmer on each cell in its own thread.
def run_glimmer_threaded():
    threads = []
    save_state(get_state(cells))
    for cell in cells:
        t = threading.Thread(target=glimmer, args=(cell, 0, [], cells.copy()))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # print shortest element in solutions
    if solutions:
        # print number of solutions
        print(len(solutions))
        solutions.sort(key=len)
        print (solutions[0])
    else:
        print('No solutions found')

if __name__ == '__main__':
    test_glimmer()
    run_glimmer_threaded()


