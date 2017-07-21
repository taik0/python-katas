#!/usr/bin/env python

from table import Table
from block import Block
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
        pass

    def PutOnTable(self, item):
        """
        pon el objeto X en el suelo (espacio no definido)
        """
        pass

    def FindSpace(self, item):
        """
        haz sitio sobre el objeto X
        """
        pass

    def FindSpaceOnTable(self):
        """
        encuentra la primer columna con espacio en el suelo
        """
        for i in range(self._table.height):
            if self._table.is_empty(i, 0):
                return i
        return -1

    def Move(self, item, col):
        """
        mueve el objeto X a la columna Y (y apilalo)
        """
        picked = self._table.get(item)
        if picked == None:
            return False
        self._table.grid[picked.col][picked.row] = ''
        next_row = self._table.next_empty(col)
        self._table.set(col, next_row, picked)
        self.picked = ''
        return True

    def Ungrasp(self, item):
        """
        suelta el bloque X
        """
        self.picked = ''

    def ClearTop(self, item):
        """
        despeja la parte superior del objeto X
        """
        pass

    def pickable(self, item):
        obj = self._table.get(item)
        if self._table.next_empty(obj.col) -1 == obj.row or obj.row == self._table.height -1:
            return True
        return False

    def Grasp(self, item):
        """
        pilla el bloque X
        """
        pass
        
    # def Pick(self, item):
    #     """
    #     pilla el bloque X
    #     """
    #     if not self.pickable(item):
    #         print "Cannot pick the block"
    #         return False
    #     self.picked = self._table.get(item)
    #     if self.picked == None:
    #         return False
    #     self._table.grid[self.picked.col][self.picked.row] = ''
    #     return True

    def GetRidOf(self, item):
        """
        saca el objeto X del medio (edited)
        """
        dest = self.FindSpaceOnTable()
        if dest < 0:
            return "No space to get rid of the block"
        self.Move(item, dest)


if __name__ == '__main__':
    t = Table(5,5)
    t.set(0,0, Block('B0000'))
    t.set(0,1, Block('B0001'))
    t.set(1,0, Block('B0002'))
    t.set(1,1, Block('B0003'))

    #helper.init_table(t, 4)

    arm = Crane(t)
    print arm
    arm.Move('B0001', 1)
    print arm
    arm.Move('B0000', 2)
    print arm
    arm.GetRidOf('B0001')
    arm.GetRidOf('B0003')
    print arm
    print arm.FindSpaceOnTable()
