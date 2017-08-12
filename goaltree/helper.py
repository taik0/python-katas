#!/usr/bin/env python

from block import Block
import random

def blockgen(n):
    block_list = []
    for i in range(n):
        blk = 'B' + str(i).zfill(4)
        block_list.append(Block(blk))
    random.shuffle(block_list)
    return block_list

def random_col(t):
    col = random.randint(0, int((t.width -1) * 0.75))
    next_row = t.next_empty(col)
    while next_row < 0:
        col = random.randint(0, int((t.width -1) * 0.75))
        next_row = t.next_empty(col)
    return col, next_row

def init_table(t, n):
    if n > t.height * t.width * (1 - 0.25):
        print "Too many initial blocks"
        return None
    block_list = blockgen(n)
    while len(block_list) > 0:
        item = block_list.pop()
        col, row = random_col(t)
        t.set(col, row, item)
