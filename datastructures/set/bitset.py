#!/usr/bin/env python

class Bitset():

    def __init__(self, size = 64):
        self._value = []
        self._size = size
        self._words_total = 1 + (self._size / 64)
        for n in range(self._words_total):
            self._value.append(0)

    def __str__(self):
        return str(map(int, self._value))

    def Add(self, item):
        idx = ( item % self._size ) // 64
        pos = ( item % self._size ) % 64
        self._value[idx] |= ( 1 << pos)

    def Size(self):
        return self._size

    def Contains(self, item):
        idx = ( item % self._size ) // 64
        pos = ( item % self._size ) % 64
        return (self._value[idx]&(1<<pos)!=0)
