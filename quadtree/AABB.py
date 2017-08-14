#!/usr/bin/env python

class Coord():

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

class AxisAlignedBoundingBox():

    def __init__(self, center, halfSize):
        """
        center: Coord
        halfSize: float
        """
        self.center = center
        self.halfSize = halfSize

    def containsPoint(self, coord):
        """
        coord: Coord
        """
        return abs(self.center.x - coord.x) <= self.halfSize and abs(self.center.y - coord.y) <= self.halfSize

    def intersectsAxisBox(self, aabb):
        """
        aabb: AxisAlignedBoundingBox
        """
        return abs(self.center.x - aabb.center.x) * 2 < (self.halfSize + aabb.halfSize) and abs(self.center.y - aabb.center.y) * 2 < (self.halfSize + aabb.halfSize)

if __name__ == '__main__':
    coord = Coord(1,1)
    coord2 = Coord(2,2)
    aabb = AxisAlignedBoundingBox(coord, 2)
    aabb2 = AxisAlignedBoundingBox(coord2, 2)
    print aabb.containsPoint(coord)
    print aabb.intersectsAxisBox(aabb2)
