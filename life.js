// Conway's Game of Life

// Create a 20x20 grid
var grid = new Array(20);
for (var i = 0; i < 20; i++) {
    grid[i] = new Array(20);
    }

// populate the grid with random cells
for (var i = 0; i < 20; i++) {
    for (var j = 0; j < 20; j++) {
        grid[i][j] = Math.random() > 0.5 ? '*' : ' ';
        }
    }

// apply the rules to the grid
function update() {
    var next = new Array(20);
    for (var i = 0; i < 20; i++) {
        next[i] = new Array(20);
        }
    for (var i = 0; i < 20; i++) {
        for (var j = 0; j < 20; j++) {
            var neighbors = countNeighbors(i, j);
            if (grid[i][j] == '*') {
                if (neighbors < 2 || neighbors > 3) {
                    next[i][j] = ' ';
                    }
                else {
                    next[i][j] = '*';
                    }
                }
            else {
                if (neighbors == 3) {
                    next[i][j] = '*';
                    }
                else {
                    next[i][j] = ' ';
                    }
                }
            }
        }
    grid = next;
    }

// count the number of neighbors around a cell
function countNeighbors(x, y) {
    var sum = 0;
    for (var i = -1; i < 2; i++) {
        for (var j = -1; j < 2; j++) {
            sum += grid[(x + i + 20) % 20][(y + j + 20) % 20] == '*' ? 1 : 0;
            }
        }
    sum -= grid[x][y] == '*' ? 1 : 0;
    return sum;
    }
