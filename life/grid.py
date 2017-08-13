#!/usr/bin/env python

"""
Grid class
"""

DEAD = 0
LIVE = 1

class Grid:
    """
    Implementation of 2D grid of cells
    Includes boundary handling
    """

    def __init__(self, grid_height, grid_width, initial = None):
        """
        Initializes grid to be DEAD, take height and width of grid as parameters
        Indexed by rows (left to right), then by columns (top to bottom)
        """
        self._height = grid_height
        self._width = grid_width
        if initial == None:
            self._cells = [[DEAD for dummy_col in range(self._width)]
                            for dummy_row in range(self._height)]
        else:
            self._cells = [[initial[row][col] for col in range(self._width)]
                            for row in range(self._height)]

    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ''
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row][col] == LIVE:
                    ans += '*'
                else:
                    ans += ' '
            ans += "\n"
        return ans

    def clone(self):
        return Grid(self._height, self._width, self._cells)

    def get_height(self):
        """
        Return the height of the grid for use in the GUI
        """
        return self._height

    def get_width(self):
        """
        Return the width of the grid for use in the GUI
        """
        return self._width


    def clear(self):
        """
        Clears grid to be DEAD
        """
        self._cells = [[DEAD for dummy_col in range(self._width)]
                       for dummy_row in range(self._height)]

    def set(self, row, col, state):
        """
        Set cell with index (row, col) to be DEAD
        """
        self._cells[row][col] = state

    def is_DEAD(self, row, col):
        """
        Checks whether cell with index (row, col) is DEAD
        """
        return self._cells[row][col] == DEAD

    def live_neighbors(self, row, col):
        cells = self.neighbors(row, col)
        alive = 0
        for cell in cells:
            if not self.is_DEAD(cell[0], cell[1]):
                alive +=1
        return alive

    def neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        ans.append(((row - 1 % self._height), col))
        ans.append((row + 1 % self._height, col))
        ans.append((row, col - 1 % self._width))
        ans.append((row, col + 1 % self._width))
        ans.append((row - 1 % self._height, col - 1 % self._width))
        ans.append((row - 1 % self._height, col + 1 % self._width))
        ans.append((row + 1 % self._height, col - 1 % self._width))
        ans.append((row + 1 % self._height, col + 1 % self._width))
        return ans

    def get_index(self, point, cell_size):
        """
        Takes point in screen coordinates and returns index of
        containing cell
        """
        return (point[1] / cell_size, point[0] / cell_size)
