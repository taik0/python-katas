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
        for child in self.children:
            ans += str(child) + ','.join(points)
        return ans + "]"

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
    coord = Coord(2,2)
    aabb = AxisAlignedBoundingBox(coord, 2)
    coord2 = Coord(1,1)
    aabb2 = AxisAlignedBoundingBox(coord2, 1)
    quad = QuadTree(aabb)
    print quad.insert(coord)
    print quad.queryRange(aabb2)
