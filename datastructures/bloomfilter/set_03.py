#!/usr/bin/env python

# Trampa, deberia usar un diccionario

class Kset():

    def __init__(self):
        self._values = set([])

    def __iter__(self):
        for item in self._values:
            yield item

    def Add(self, item):
        self._values.add(item)

    def Size(self):
        return len(self._values)

    def Contains(self, item):
        return True if item in self._values else False
