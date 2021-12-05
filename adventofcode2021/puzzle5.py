import re

def delta(x): return 0 if x == 0 else int(x/abs(x))

def draw_line(start, dest, grid):
    dx, dy = (delta(dest[0] - start[0]), delta(dest[1] - start[1]))
    x, y = start

    while True:
        grid[y][x] += 1
        if (x,y) == dest: break
        x += dx
        y += dy

with open('puzzle5.dat') as f:
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for line in f:
        m = re.match(r'(\d+),(\d+)\s\-\>\s(\d+),(\d+)', line.strip())
        start, dest = (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))
        draw_line(start, dest, grid)
    print(sum(sum(1 for x in row if x > 1) for row in grid))
