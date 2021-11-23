#!/usr/bin/python

# 1. 1 ->
# 2.

from random import randint, random, choice

houses = ['No Houses', '1 House', '2 Houses', '3 Houses', '4 Houses', 'Hotel']
motion = {-1: 'move backward', 0: 'stay put', 1: 'move forward'}
# (state,mark,state1,mark1,dir)

statevals = 20
cellvals = 5
maxstates = (statevals+1)*(cellvals+1)
maxchromos = 2000

chromos = []
cfitness = []

bestprog = None
bestfit = 1


def makeChromosone():
    prog = {}
    for state in range(statevals+1):
        for cell in range(cellvals+1):
            dst = (randint(0, statevals)-state,
                   randint(0, cellvals), 2*randint(0, 1)-1)
            prog[(state, cell)] = dst
    return prog


def runprog(prog, tape, seen):
    state = 0
    pc = 0
    for i in range(50):
        if pc not in tape:
            tape[pc] = 0
        ins = (state, tape[pc])
        if ins not in prog:
            return False
        dst = prog[ins]
        seen[ins] = dst
        state = state+dst[0]
        tape[pc] = dst[1]
        pc = pc + dst[2]
    return True


def score(prog):
    global bestprog, bestfit

    fitness = 1
    seen = {}
    worksfor = {}

    for p1 in range(3):
        for p2 in range(3):
            tape = {}
            tape[-1] = p1
            tape[1] = p2
            tape[0] = 0

            if not runprog(prog, tape, seen):
                continue

            if tape[0] == (p1*p2):
                worksfor[(p1, p2)] = 1
                fitness = fitness+1

    if fitness > bestfit or (bestprog is not None and fitness == bestfit and len(seen) < len(bestprog)):
        bestprog = seen
        bestfit = fitness
        print ("best fitness now:", bestfit)

        fn = 'fit%02d.txt' % (bestfit)
        f = open(fn, 'w')
        for v in worksfor.keys():
            f.write("solves %d * %d\n" % (v[0], v[1]))
        ks = seen.keys()
        ks.sort()
        for k in ks:
            v = seen[k]
            row = []
            row.append('"$%d"' % k[0])
            row.append('"%s"' % houses[k[1]])
            actions = []
            if v[0] < 0:
                if (k[0]+v[0]) == 0:
                    actions.append('give all your money to the bank')
                else:
                    actions.append('pay $%d to the bank' % (-v[0]))
            elif v[0] > 0:
                actions.append('take $%d from the bank' % v[0])
            if k[1] != v[1]:
                if k[1] == 5:
                    if v[1] == 0:
                        actions.append('remove the hotel')
                    elif v[1] == 1:
                        actions.append('replace the hotel with a house')
                    else:
                        actions.append(
                            'replace the hotel with %d houses' % v[1])
                elif k[1] == 0:
                    if v[1] == 5:
                        actions.append('build a hotel')
                    elif v[1] != 1:
                        actions.append('build %d houses' % v[1])
                    else:
                        actions.append('build a house')
                elif v[1] == 5:
                    if k[1] == 1:
                        actions.append('build a hotel in place of the house')
                    else:
                        actions.append('build a hotel in place of the houses')
                elif v[1] == 0:
                    if k[1] != 1:
                        actions.append('remove all the houses')
                    else:
                        actions.append('remove the house')
                elif v[1] > k[1]:
                    if (v[1]-k[1]) == 1:
                        actions.append('build a house')
                    else:
                        actions.append('build %d houses' % (v[1]-k[1]))
                else:
                    if (k[1]-v[1]) == 1:
                        actions.append('remove a house')
                    else:
                        actions.append('remove %d houses' % (k[1]-v[1]))
            if v[2] > 0:
                actions.append('move forward')
            elif v[2] < 0:
                actions.append('move backward')
            if len(actions) == 0:
                row.append('"do nothing (this should never happen)"')
            elif len(actions) == 1:
                row.append('"%s"' % actions[0])
            elif len(actions) == 2:
                row.append('"%s and %s"' % (actions[0], actions[1]))
            else:
                row.append('"%s, %s and %s"' %
                           (actions[0], actions[1], actions[2]))
            f.write(','.join(row))
            f.write('\n')
        f.close()

    return fitness


def ranChromo():
    return choice(chromos)


for i in range(maxchromos):
    c = makeChromosone()
    chromos.append(c)
    f = score(c)
    cfitness.append((f, i))

gen = 0
while True:
    gen = gen + 1
    print("Gen %d" % gen)
    newChromo = []
    for i in range((2*maxchromos)/3):
        if random() < 0.25:
            c3 = makeChromosone()
        else:
            c1 = ranChromo()
            c2 = ranChromo()
            c3 = {}
            for k in c1:
                c3[k] = c1[k]
            for k in c2:
                c3[k] = c2[k]
        newChromo.append(c3)
    cfitness.sort()
    for i in range(len(newChromo)):
        c = newChromo[i]
        d = cfitness[i]
        f = score(c)
        chromos[d[1]] = c
        cfitness[i] = (f, d[1])
