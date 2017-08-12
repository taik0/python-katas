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
        self._grid_height = grid_height
        self._grid_width = grid_width
        if initial == None:
            self._cells = [[DEAD for dummy_col in range(self._grid_width)]
                            for dummy_row in range(self._grid_height)]
        else:
            self._cells = [[initial[col][row] for col in range(self._grid_width)]
                            for row in range(self._grid_height)]

    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ""
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._cells[row][col] == LIVE:
                    ans += '*'
                else:
                    ans += ' '
            ans += "\n"
        return ans

    def clone(self):
        return Grid(self._grid_height, self._grid_width, self._cells)

    def get_grid_height(self):
        """
        Return the height of the grid for use in the GUI
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Return the width of the grid for use in the GUI
        """
        return self._grid_width


    def clear(self):
        """
        Clears grid to be DEAD
        """
        self._cells = [[DEAD for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]

    def set_DEAD(self, row, col):
        """
        Set cell with index (row, col) to be DEAD
        """
        self._cells[row][col] = DEAD

    def set_LIVE(self, row, col):
        """
        Set cell with index (row, col) to be LIVE
        """
        self._cells[row][col] = LIVE

    def is_DEAD(self, row, col):
        """
        Checks whether cell with index (row, col) is DEAD
        """
        return self._cells[row][col] == DEAD

    def neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))
        if (row > 0) and (col < self._grid_width - 1):
            ans.append((row - 1, col + 1))
        if (row < self._grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))
        if (row < self._grid_height - 1) and (col < self._grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans

    def get_index(self, point, cell_size):
        """
        Takes point in screen coordinates and returns index of
        containing cell
        """
        return (point[1] / cell_size, point[0] / cell_size)
