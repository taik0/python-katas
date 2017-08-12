#!/usr/bin/env python

from table import Table
from block import Block
from goaltree import GoalTree
import helper

class Crane():

    def __init__(self, t):
        self._table = t

    def __str__(self):
        return str(self._table)

    def PutOn(self, item1, item2):
        """
        pon el objeto X encima del objeto Y
        """
        message = 'PutOn %s %s' % (item1, item2)
        dest = self._table.get(item2)
        return GoalTree(message, [ self.FindSpace(item2), self.Grasp(item1), self.Move(item1, dest.col), self.Ungrasp(item1) ])

    def PutOnTable(self, item):
        """
        pon el objeto X en el suelo (espacio no definido)
        """
        message = 'PutOnTable %s' % (item)
        dest = self.FindSpaceOnTable()
        if dest < 0:
            raise "No space to get rid of the block"
        return GoalTree(message, [ self.Grasp(item), self.Move(item, dest), self.Ungrasp(item) ])

    def FindSpace(self, item):
        """
        haz sitio sobre el objeto X
        """
        message = 'FindSpace %s' % (item)
        if self.pickable(item):
            return GoalTree(message)
        return GoalTree(message, [ self.ClearTop(item), self.FindSpace(item) ])

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
        picked = self._table.get(item)
        if picked == None:
            raise Exception("Cant move")
        self._table.grid[picked.col][picked.row] = None
        next_row = self._table.next_empty(col)
        self._table.set(col, next_row, picked)
        return GoalTree(message)

    def Ungrasp(self, item):
        """
        suelta el bloque X
        """
        message = 'Ungrasp %s' % (item)
        return GoalTree(message)

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
        for row in range(blk.row +1, self._table.height):
            if self._table.grid[blk.col][row] != None:
                stack.append(self._table.grid[blk.col][row].name)
        while len(stack) > 0:
            new_blk = stack.pop()
            gtree.add_child(self.GetRidOf(new_blk))
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
        return gtree

    def GetRidOf(self, item):
        """
        saca el objeto X del medio (edited)
        """
        message = 'GetRidOf %s' % (item)
        gtree = GoalTree(message)
        if self._table.get(item) != None:
            gtree.add_child(self.PutOnTable(item))
        return gtree


if __name__ == '__main__':
    t = Table(22,5)
    helper.init_table(t, 30)
    arm = Crane(t)
    print arm
    x = arm.PutOn('B0025', 'B0003')
    print "Why PutOn B0025 B0003? ", x.Why('PutOn B0025 B0003')
    print "How PutOn B0025 B0003? ", x.How('PutOn B0025 B0003')
    print "How Grasp B0025? ", x.How('Grasp B0025')
    print "Why ClearTop B0025? ", x.Why('ClearTop B0025')
    print "How Ungrasp B0025?", x.How('Ungrasp B0025')
    print "How Fuck the police? ", x.How('Fuck the police')
    print arm
