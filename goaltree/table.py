#!/usr/bin/env python

class Table():

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.grid = [[None for dummy_row in range(self.height)]
                       for dummy_col in range(self.width)]

    def __str__(self):
        lines = []
        for i in range(self.height -1 , -1 , -1):
            lines.append('\t'.join([str(self.grid[j][i]) for j in range(self.width)]))
        return '\n'.join(lines)

    def _is_valid(self, col, row):
        return col >= 0 and col < self.width and row >= 0 and row < self.height and self.grid[col][row] == None and (row == 0 or self.grid[col][row-1] != None)

    def is_empty(self, col, row):
        if self.grid[col][row] == None:
            return True
        return False

    def _is_block(self, obj):
        try:
            a = obj.name
            return True
        except:
            return False

    def set(self, col, row, obj):
        assert self._is_valid(col, row)
        assert self._is_block(obj)
        self.grid[col][row] = obj
        obj.set_pos(col, row)
        return True

    def get(self, id):
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j] != None:
                    if self.grid[i][j].name == id:
                        return self.grid[i][j]
        return None

    def next_empty(self, col):
        for i in range(self.height):
            if self.grid[col][i] == None:
                return i
        return -1

if __name__ == '__main__':
    t = Table(3,3)
    from block import Block
    b = Block('B000')
    c = Block('B001')
    print t.set(0,0,b)
    print t.set(1,0,c)
    print t
