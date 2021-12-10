from statistics import median
from functools import reduce

delims = '()[]{}<>'
corrupt_scores = {')': 3, ']': 57, '>': 25137, '}': 1197}

def read_input():
    with open('puzzle10.dat', 'r') as f:
        for line in f:
            yield line.strip()

def score_line(line):
    stack = []
    for c in line:
        pos = delims.find(c)
        val = pos // 2 + 1
        if pos % 2 == 1:
            if not stack or stack[-1] != val:
                return corrupt_scores[c], 0
            stack.pop()
        else:
            stack.append(val)

    return 0, reduce(lambda x, y: x * 5 + y, stack[::-1]) if stack else 0

# Part 1
print(sum(score_line(line)[0] for line in read_input()))

# Part 2
print(median(score_line(line)[1]
             for line in read_input() if score_line(line)[1] > 0))
