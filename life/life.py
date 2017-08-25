#!/usr/bin/env python

from grid import Grid
from grid import LIVE, DEAD

class Life():

    def __init__(self, grid):
        """
        The grid is an object with the seed for the game
        """
        self._grid = grid

    def __str__(self):
        return str(self._grid)

    def evo(self, row, col):
        """
        Return DEAD or LIVE for the next state of the cell
        """
        n = self._grid.live_neighbors(row, col)
        if self._grid.is_DEAD(row, col):
            return LIVE if n == 3 else DEAD
        else:
            if n < 2:
                return DEAD
            elif n > 3:
                return DEAD
            else:
                return LIVE

    def tick(self):
        new_grid = self._grid.clone()
        visited = Grid(self._grid._height, self._grid._width)
        visited.set(0,0, LIVE)
        q = [ (0,0) ]

        while len(q) > 0:
            current = q.pop(0)
            for neighbor in self._grid.neighbors(current[0], current[1]):
                if visited.is_DEAD(neighbor[0], neighbor[1]):
                    new_grid.set(neighbor[0], neighbor[1], self.evo(neighbor[0], neighbor[1]))
                    visited.set(neighbor[0], neighbor[1], LIVE)
                    q.append((neighbor[0], neighbor[1]))

        self._grid = new_grid

if __name__ == '__main__':
    initial = Grid(20,20)
    # Beacon
    initial.set(2,1, LIVE)
    initial.set(2,2, LIVE)
    initial.set(3,1, LIVE)
    initial.set(3,2, LIVE)
    initial.set(4,3, LIVE)
    initial.set(4,4, LIVE)
    initial.set(5,3, LIVE)
    initial.set(5,4, LIVE)

    # Blinker
    initial.set(9,1, LIVE)
    initial.set(9,2, LIVE)
    initial.set(9,3, LIVE)


    game = Life(initial)
    import time

    for i in range(10):
        print game
        game.tick()
        time.sleep(1)



    print game
