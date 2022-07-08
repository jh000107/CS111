#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *
from gol_graphics import *
import random

def count_neighbors(cellr, cellc, grid):
    """ returns the number of alive neighbors of the cell at position
        [cellr][cellc] in the specified grid
        inputs: cellr and cellc should be representing index numbers
                grid is a 2-D list
    """
    count = 0
    for r in range(cellr-1, cellr+2):
        for c in range(cellc-1, cellc+2):
            if grid[r][c] == 1:
                count += 1
    if grid[cellr][cellc] == 1:
                count -= 1
    return count

def next_gen(grid):
    """ uses the rules of the Game of Life to create and return a
        new 2-D list representing the next generation of cells
        input: grid is a 2-D list
    """
    new_grid = copy(grid)
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            if grid[r][c] == 1:
                if count_neighbors(r, c, grid) < 2:
                    new_grid[r][c] = 0
                elif count_neighbors(r, c, grid) > 3:
                    new_grid[r][c] = 0
            else:
                if count_neighbors(r, c, grid) == 3:
                    new_grid[r][c] = 1
    return new_grid
            
