#!/usr/bin/env python

class Table():

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [['' for dummy_row in range(self.width)]
                       for dummy_col in range(self.height)]

    def __str__(self):
        lines = []
        for i in range(self.width -1 , -1 , -1):
            line = ''
            for j in range(self.height):
                line += str(self.grid[j][i]) + '\t'
            lines.append(line)
        return '\n'.join(lines)

    def _is_valid(self, col, row):
        return col >= 0 and col < self.width and row >= 0 and row < self.height and self.grid[col][row] == '' and (row == 0 or self.grid[col][row-1] != '')

    def is_empty(self, col, row):
        if self.grid[col][row] == '':
            return True
        return False

    def set(self, col, row, obj):
        if not self._is_valid(col, row):
            print "fail to set"
            return False
        self.grid[col][row] = obj
        if obj != '':
            obj.set_pos(col, row)
        return True

    def get(self, id):
        for i in range(self.height):
            for j in range(self.width):
                if not self.is_empty(i, j):
                    if self.grid[i][j].name == id:
                        return self.grid[i][j]
        return None

    def next_empty(self, col):
        for i in range(self.height):
            if self.is_empty(col, i):
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
