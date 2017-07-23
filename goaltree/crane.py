#!/usr/bin/env python

from table import Table
from block import Block
from goaltree import GoalTree
import helper

class Crane():

    def __init__(self, t):
        self._table = t
        self.picked = ''

    def __str__(self):
        return str(self._table)

    def PutOn(self, item1, item2):
        """
        pon el objeto X encima del objeto Y
        """
        message = 'PutOn %s %s' % (item1, item2)
        gtree = GoalTree(message)
        dest = self._table.get(item2)
        gtree.add_child(self.FindSpace(item2))
        gtree.add_child(self.Grasp(item1))
        gtree.add_child(self.Move(item1, dest.col))
        gtree.add_child(self.Ungrasp(item1))
        for child in gtree.children():
            child.set_parent(message)
        return gtree

    def PutOnTable(self, item):
        """
        pon el objeto X en el suelo (espacio no definido)
        """
        message = 'PutOnTable %s' % (item)
        gtree = GoalTree(message)
        dest = self.FindSpaceOnTable()
        if dest < 0:
            return "No space to get rid of the block"
        gtree.add_child(self.Grasp(item))
        gtree.add_child(self.Move(item, dest))
        gtree.add_child(self.Ungrasp(item))
        for child in gtree.children():
            child.set_parent(message)
        return gtree

    def FindSpace(self, item):
        """
        haz sitio sobre el objeto X
        """
        message = 'FindSpace %s' % (item)
        gtree = GoalTree(message)
        if self.pickable(item):
            return gtree
        gtree.add_child(self.ClearTop(item))
        gtree.add_child(self.FindSpace(item))
        for child in gtree.children():
            child.set_parent(message)
        return gtree

    def FindSpaceOnTable(self):
        """
        encuentra la primer columna con espacio en el suelo
        """
        for i in range(self._table.width):
            if self._table.is_empty(i, 0):
                return i
        return -1

    def Move(self, item, col):
        """
        mueve el objeto X a la columna Y (y apilalo)
        """
        message = 'Move %s %i' % (item, col)
        gtree = GoalTree(message)
        picked = self._table.get(item)
        if picked == None:
            return False
        self._table.grid[picked.col][picked.row] = ''
        next_row = self._table.next_empty(col)
        self._table.set(col, next_row, picked)
        self.picked = ''
        return gtree

    def Ungrasp(self, item):
        """
        suelta el bloque X
        """
        self.picked = ''
        message = 'Ungrasp %s' % (item)
        gtree = GoalTree(message)
        return gtree

    def ClearTop(self, item):
        """
        despeja la parte superior del objeto X
        """
        message = 'ClearTop %s' % (item)
        gtree = GoalTree(message)
        stack = []
        blk = self._table.get(item)
        if self.pickable(blk.name):
            return gtree
        for row in range(blk.row + 1, self._table.width):
            if self._table.grid[blk.col][row] != '':
                stack.append(self._table.grid[blk.col][row].name)
        while len(stack) > 0:
            new_blk = stack.pop()
            gtree.add_child(self.GetRidOf(new_blk))
        for child in gtree.children():
            child.set_parent(message)
        return gtree


    def pickable(self, item):
        obj = self._table.get(item)
        if self._table.next_empty(obj.col) -1 == obj.row or obj.row == self._table.height -1:
            return True
        return False

    def Grasp(self, item):
        """
        pilla el bloque X
        """
        message = 'Grasp %s' % (item)
        gtree = GoalTree(message)
        if self._table.get(item) != None:
            gtree.add_child(self.ClearTop(item))
            for child in gtree.children():
                child.set_parent(message)
        return gtree

    def GetRidOf(self, item):
        """
        saca el objeto X del medio (edited)
        """
        message = 'GetRidOf %s' % (item)
        gtree = GoalTree(message)
        if self._table.get(item) != None:
            gtree.add_child(self.PutOnTable(item))
            for child in gtree.children():
                child.set_parent(message)
        return gtree


if __name__ == '__main__':
    t = Table(15,15)
    t.set(0,0, Block('B0000',0 ,0))
    t.set(0,1, Block('B0001', 0, 1))
    t.set(0,2, Block('B0004', 0, 2))
    t.set(0,3, Block('B0005', 0, 3))
    t.set(0,4, Block('B0006', 0, 4))
    t.set(1,0, Block('B0002', 1, 0))
    t.set(1,1, Block('B0003', 1, 1))

    #helper.init_table(t, 4)

    arm = Crane(t)
    print arm
    x = arm.PutOn('B0006', 'B0003')
    print x.Why('PutOn B0006 B0003')
    print x.How('PutOn B0006 B0003')
    print x.How('Grasp B0006')
    print x.Why('ClearTop B0006')
    print x.How('Ungrasp B0006')
    print x.How('Fuck the police')

    print "---"
