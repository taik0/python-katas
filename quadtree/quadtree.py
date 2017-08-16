#!/usr/bin/env python

from AABB import AxisAlignedBoundingBox, Coord

class QuadTree():

    def __init__(self, boundary):
        """
        boundary: AxisAlignedBoundingBox
        """
        self.boundary = boundary
        self.points = []
        self.children = []

    def __iter__(self):
        for child in self.children:
            yield child

    def __str__(self):
        ans = "["
        for point in self.points:
            ans += ' (' + str(point.x) + ', ' + str(point.y) + ') '
        for child in self:
            ans += str(child)
        return ans + "]\n"

    def insert(self, coord):
        """
        coord = Coord
        """
        if not self.boundary.containsPoint(coord):
            return False

        if len(self.points) < 4:
            self.points.append(coord)
            return True

        if len(self.children) < 1:
            self.subdivide()

        for child in self:
            if child.insert(coord):
                return True

        return False

    def subdivide(self):
        if len(self.children) > 0:
            return False

        if self.boundary.halfSize == 1:
            return False

        size = self.boundary.halfSize / 2
        # NW
        self.children.append(QuadTree(AxisAlignedBoundingBox(Coord(self.boundary.center.x, self.boundary.center.y), size)))
        # NE
        self.children.append(QuadTree(AxisAlignedBoundingBox(Coord(self.boundary.center.x + size, self.boundary.center.y), size)))
        # SW
        self.children.append(QuadTree(AxisAlignedBoundingBox(Coord(self.boundary.center.x, self.boundary.center.y + size), size)))
        # SE
        self.children.append(QuadTree(AxisAlignedBoundingBox(Coord(self.boundary.center.x + size, self.boundary.center.y + size), size)))
        while len(self.points) > 0:
            point = self.points.pop(0)
            for child in self:
                if child.boundary.containsPoint(point):
                    child.insert(point)




    def queryRange(self, range):
        """
        range: AxisAlignedBoundingBox
        """
        points_in_range = []
        if not self.boundary.intersectsAxisBox(range):
            return points_in_range

        for point in self.points:
            if range.containsPoint(point):
                points_in_range.append(point)

        if len(self.children) < 1:
            return points_in_range

        for child in self:
            points_in_range += child.queryRange(range)

        return points_in_range

if __name__ == '__main__':
    coord = Coord(1,1)
    aabb = AxisAlignedBoundingBox(coord, 1)
    #
    coord2 = Coord(0,0)
    coord3 = Coord(3,3)
    #
    coord4 = Coord(1,2)
    coord5 = Coord(2,3)
    coord6 = Coord(3,1)
    #
    coord7 = Coord(2,1)
    coord8 = Coord(2,2)
    coord9 = Coord(0,1)
    coord10 = Coord(1,0)
    coord11 = Coord(2,0)
    quad = QuadTree(aabb)
    #
    print quad.insert(coord2)
    print quad.insert(coord3)
    #
    print quad.insert(coord4)
    #
    print quad.insert(coord)
    print quad.insert(coord5)
    print quad.insert(coord6)
    #
    print quad.insert(coord7)
    print quad.insert(coord8)
    print quad.insert(coord9)
    print quad.insert(coord10)
    print quad.insert(coord11)
    print "children: ", quad.children
    print "points:", quad.points
    print quad
    for q in quad.children:
        print q.boundary.center.x, q.boundary.center.y
