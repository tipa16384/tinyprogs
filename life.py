# implement Conway's Game of Life using the ncurses library

import random

# create a 100x100 grid
# randomly populate it with cells
# display the grid
# every second, apply the rules of the game to the grid
#   - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#   - Any live cell with two or three live neighbours lives on to the next generation.
#   - Any live cell with more than three live neighbours dies, as if by overcrowding.
#   - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# create grid
def create_grid(height, width):
    grid = []
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(0)
    return grid

# populate grid with random cells
def populate_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = random.randint(0, 1)
    return grid

# display grid
def display_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                print(' ', end='')
            else:
                print('*', end='')
        print()

# displat the grid with ncurses
def display_grid_ncurses(grid):
    import curses
    curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(11, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(12, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(13, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(14, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(15, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(16, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(17, curses.COLOR_WHITE, curses.COLOR_BLACK)
    display_grid_ncurses_helper(grid, 0, 0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()



# apply rules of the game to the grid
def apply_rules(grid):
    new_grid = create_grid(len(grid), len(grid[0]))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # count the number of live neighbors
            neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if i + x >= 0 and i + x < len(grid) and j + y >= 0 and j + y < len(grid[i]):
                        if grid[i + x][j + y] == 1:
                            neighbors += 1
            # apply rules
            if grid[i][j] == 1:
                if neighbors < 2:
                    new_grid[i][j] = 0
                elif neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = 1
                elif neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

if __name__ == '__main__':
    grid = create_grid(10, 10)
    grid = populate_grid(grid)
    display_grid(grid)
    while True:
        grid = apply_rules(grid)
        display_grid(grid)
        