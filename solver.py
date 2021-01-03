"""My sudoku solver."""
import numpy as np

grid = [
    [4, 0, 0, 8, 7, 0, 0, 2, 0],
    [0, 8, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 6, 3, 0, 0, 8, 0, 1],
    [7, 0, 0, 1, 0, 0, 0, 8, 0],
    [6, 1, 2, 0, 9, 8, 7, 3, 4],
    [0, 0, 0, 0, 6, 0, 0, 1, 9],
    [1, 9, 3, 4, 2, 7, 5, 0, 0],
    [8, 0, 7, 0, 1, 0, 3, 0, 2],
    [0, 2, 0, 0, 0, 3, 0, 0, 0]
]

matrix = np.matrix(grid)
print(matrix)
print("\n")



def is_possible_value(y, x, value):
    """Find if a value is possible at a specific location."""
    global grid
    # Test for row
    if value in grid[y]:
        return False

    # Test for columns
    for i in range(9):
        if grid[i][x] == value:
            return False

    # Test for sub 3x3 grid
    x = (x // 3) * 3
    y = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[y+i][x+j] == value:
                return False
    return True


def solve():
    """Solve the matrix."""
    global grid
    # Loop over all 9x9 values for '0' value
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                # Check pour 1-9, if possible and continue solving. If not, backtrack
                for nb in range(1, 10):
                    if is_possible_value(y, x, nb):
                        grid[y][x] = nb
                        solve()
                        grid[y][x] = 0
                return
    matrix = np.matrix(grid)
    print(matrix)

solve()

