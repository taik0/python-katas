#!/usr/bin/env python

import math
# bitset

from bitset import Bitset
from hasher import Hasher


class Hashedbitset():

    def __init__(self, size):
        self._value = Bitset(size)
        self._size = size
        self._hasher = Hasher()

    def Add(self, item):
        n = self._hasher.hash(item, 1, self._size)[0]
        self._value.Add(n)

    def Size(self):
        return self._value.Size()

    def Contains(self, item):
        n = self._hasher.hash(item, 1, self._size)[0]
        return self._value.Contains(n)
