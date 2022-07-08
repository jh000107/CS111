#
# ps8pr2.py (Problem Set 8, Problem 2)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: This file is for your solutions to Problem 2.
# Your solutions to Problem 1 should go in ps8pr1.py instead.

from ps8pr1 import *
from gol_graphics import *

def has_left_right_neighbor(grid):
            """gets a grid and applies the left right neighbor rule to every
               cells.
            """
            new_grid = copy(grid)
            width = len(grid)
            height = len(grid[0])
            for r in range(1,height-1):
                        for c in range(1,width-1):
                                    if (grid[r][c-1] == 1) or (grid[r][c+1] == 1):
                                                new_grid[r][c] = 1
                                    else:
                                               new_grid[r][c] = 0
            return new_grid

def count_neighbors(cellr, cellc, grid):
            """gets a grid and the position of a specific cell and tells how
               many cells are alive within the neighbor of that cells.
            """
            new_grid = copy(grid)
            width = len(grid)
            height = len(grid[0])
            count = 0
            if grid[cellr][cellc-1] == 1:
                        count += 1
            if grid[cellr][cellc+1] == 1:
                        count += 1
            if grid[cellr-1][cellc] == 1:
                        count += 1
            if grid[cellr+1][cellc] == 1:
                        count += 1
            if grid[cellr+1][cellc-1] == 1:
                        count += 1
            if grid[cellr+1][cellc+1] == 1:
                        count += 1
            if grid[cellr-1][cellc-1] == 1:
                        count += 1
            if grid[cellr-1][cellc+1] == 1:
                        count += 1
            return count

def next_gen(grid):
            """takes a 2-D list called grid hat represents the current
               generation of cells, and uses the rules of the Game of Life to
               create and return a new 2-D list representing the next generation
               of cells.
            """
            #All cells on the outer boundary of the grid remain fixed at 0.

            #An inner cell that has fewer than 2 alive neighbors dies (because of loneliness).

            #An inner cell that has more than 3 alive neighbors dies (because of overcrowding).

            #An inner cell that is dead and has exactly 3 alive neighbors comes to life.

            #All other cells maintain their state.

            new_grid = copy(grid)
            width = len(grid)
            height = len(grid[0])
            for r in range(1,height-1):
                        for c in range(1,width-1):
                                    neighbor = count_neighbors(r, c, grid)
                                    if neighbor < 2:
                                                new_grid[r][c] = 0
                                    if neighbor > 3:
                                                new_grid[r][c] = 0
                                    if grid[r][c] == 0 and neighbor == 3:
                                                new_grid[r][c] = 1
            return new_grid
                                    
