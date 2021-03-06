#!/usr/bin/env python

from bitset import Bitset
from hasher import Hasher

class Bloomfilter():

    def __init__(self, size, keys):
        self._value = Bitset(size)
        self._size = size
        self._keys = keys
        self._hasher = Hasher()

    def Add(self, item):
        [ self._value.Add(i) for i in self._hasher.hash(item, self._keys) ]

    def Size(self):
        return self._value.Size()

    def Contains(self, item):
        n = self._hasher.hash(item, self._keys)
        for i in n:
            if not self._value.Contains(i):
                return False
        return True
