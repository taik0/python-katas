#!/usr/bin/env python

import struct
import mmh3
from fnvhash import fnv1a_64

class Hasher():

    def _hash(self, string):
        return [ self._murmur(string), self._fnv(string) ]

    def _murmur(self, string):
        return struct.unpack("L", str(mmh3.hash128(string))[:8])[0]

    def _fnv(self, string):
        return struct.unpack("L", str(fnv1a_64('hola'))[:8])[0]

    def hash(self, string, keys, size):
        s = self._hash(string)
        return [ (s[0] + s[1] * i) % size for i in range(keys) ]
