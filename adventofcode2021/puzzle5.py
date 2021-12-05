# the fifth puzzle

import re

fn = 'puzzle5.dat'

# make a 10x10 grid
grid = [[0 for x in range(1000)] for y in range(1000)]


def open_file():
    "open the file and yield the lines"
    with open(fn) as f:
        for line in f:
            yield parse_line(line.strip())


def parse_line(line):
    m = re.match(r'(\d+),(\d+)\s\-\>\s(\d+),(\d+)', line)
    assert m
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def sanity_check():
    print(grid)
    for start, dest in open_file():
        print(start, dest)


def draw_line(start, dest, exclude_diag=False):
    # draw the line
    if exclude_diag and start[0] != dest[0] and start[1] != dest[1]:
        return

    dx = dest[0] - start[0]
    if dx != 0:
        dx = int(dx/abs(dx))
    dy = dest[1] - start[1]
    if dy != 0:
        dy = int(dy/abs(dy))

    x = start[0]
    y = start[1]

    while True:
        grid[y][x] += 1
        if x == dest[0] and y == dest[1]:
            break
        x += dx
        y += dy


def score_grid():
    "return number of elements in grid that are > 1"
    return sum(sum(1 for x in row if x > 1) for row in grid)


if __name__ == "__main__":
    for start, dest in open_file():
        draw_line(start, dest, False)
    print(score_grid())
