#!/usr/bin/env python

class Node(object):

    def __init__(self, value, weight, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.weight = weight

class Leaf(object):

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
