#!/usr/bin/env python

import struct
import mmh3
from fnvhash import fnv1a_64

class Hasher():

    def _hash(self, string, hashfunc):
        return struct.unpack("L", str(hashfunc(string))[:8])[0]


    def hash(self, string, keys):
        s0 = self._hash(string, mmh3.hash128)
        s1 = self._hash(string, fnv1a_64)
        return [ ( s0 + s1 * i) for i in range(keys) ]
