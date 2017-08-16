#!/usr/bin/env python

from math import sqrt

class Coord():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class AxisAlignedBoundingBox():

    def __init__(self, center, halfSize):
        """
        center: Coord
        halfSize: float
        """
        self.center = center
        self.halfSize = halfSize

    def distance(self, coordA, coordB):
        return Coord(sqrt((coordB.x - coordA.x)**2), sqrt((coordB.y - coordA.y)**2 ))

    def containsPoint(self, coord):
        """
        coord: Coord
        """
        return abs(self.distance(self.center, coord).x) <= self.halfSize and abs(self.distance(self.center, coord).y) <= self.halfSize

    def intersectsAxisBox(self, aabb):
        """
        aabb: AxisAlignedBoundingBox
        """
        return abs(self.center.x - aabb.center.x) * 2 < (self.halfSize + aabb.halfSize) and abs(self.center.y - aabb.center.y) * 2 < (self.halfSize + aabb.halfSize)

if __name__ == '__main__':
    coord = Coord(0,0)
    coord2 = Coord(3,3)
    aabb = AxisAlignedBoundingBox(coord, 1)
    aabb2 = AxisAlignedBoundingBox(coord2, 1)
    print aabb.center.x, aabb.center.y, aabb.halfSize
    coords = [ (0,0), (0,1), (1,0), (1,1), (-1,-1), (2,2), (3,3), (-2, -2), (2,1), (1,2), (0,-1), (-1, 0),(1,-1), (-1, 1)]
    for c in coords:
        print "contains: ", c, aabb.containsPoint(Coord(c[0], c[1]))
    # print aabb.containsPoint(coord)
    # print aabb.containsPoint(coord2)
    # print aabb.intersectsAxisBox(aabb2)
