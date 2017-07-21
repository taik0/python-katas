#!/usr/bin/env python

class Block():

    def __init__(self, name, col = None, row = None):
        self.name = name
        self.col = col
        self.row = row

    def __str__(self):
        return self.name

    def set_pos(self, col, row):
        self.col = col
        self.row = row
