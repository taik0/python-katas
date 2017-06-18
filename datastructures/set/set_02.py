#!/usr/bin/env python


class Kset():

    def __init__(self):
        self._values = []

    def __iter__(self):
        for item in self._values:
            yield item

    def Add(self, item):
        if not self.Contains(item):
            self._values.append(item)

    def Size(self):
        return len(self._values)

    def Contains(self, item):
        return True if item in self._values else False
