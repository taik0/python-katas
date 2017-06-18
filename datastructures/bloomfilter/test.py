#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from set_01 import Kset as Kset_01
from set_02 import Kset as Kset_02
from set_03 import Kset as Kset_03
from set_04 import Bitset
from set_04 import Hashedbitset
from set_05 import Bloomfilter

class TestKset(unittest.TestCase):

    def testKset_01(self):
        setx = Kset_01()
        dataset = [ "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwy" ]
        dataset = dataset + dataset + dataset
        size = 24
        for t in dataset:
            setx.Add(t)
        for t in dataset:
            self.assertTrue(setx.Contains(t))
        self.assertFalse(setx.Contains("unknown data"))
        self.assertEqual(setx.Size(), size)

    def testKset_02(self):
        setx = Kset_02()
        dataset = [ "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwy" ]
        dataset = dataset + dataset + dataset
        size = 8
        for t in dataset:
            setx.Add(t)
        for t in dataset:
            self.assertTrue(setx.Contains(t))
        self.assertFalse(setx.Contains("unknown data"))
        self.assertEqual(setx.Size(), size)

    def testKset_03(self):
        setx = Kset_03()
        dataset = [ "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwy" ]
        dataset = dataset + dataset + dataset
        size = 8
        for t in dataset:
            setx.Add(t)
        for t in dataset:
            self.assertTrue(setx.Contains(t))
        self.assertFalse(setx.Contains("unknown data"))
        self.assertEqual(setx.Size(), size)

    def testBitset(self):
        setx = Bitset(256)
        dataset = [ 1, 5, 4, 10, 56, 64, 65, 128, 230, 255 ]
        dataset = dataset + dataset + dataset
        size = 256
        for t in dataset:
            setx.Add(t)
        for t in dataset:
            self.assertTrue(setx.Contains(t))
        self.assertFalse(setx.Contains(280))
        self.assertEqual(setx.Size(), size)

    def testHashedbitset(self):
        setx = Hashedbitset(500000)
        dataset = [ "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwy" ]
        dataset = dataset + dataset + dataset
        size = 500000
        for t in dataset:
            setx.Add(t)
        for t in dataset:
            self.assertTrue(setx.Contains(t))
        self.assertFalse(setx.Contains("unknown data"))
        self.assertEqual(setx.Size(), size)

    def testBloomfilter(self):
        setx = Bloomfilter(400000, 30)
        dataset = [ "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwy" ]
        dataset = dataset + dataset + dataset
        size = 400000
        for t in dataset:
            setx.Add(t)
        for t in dataset:
            self.assertTrue(setx.Contains(t))
        self.assertFalse(setx.Contains("unknown data"))
        self.assertEqual(setx.Size(), size)

if __name__ == '__main__':
    unittest.main()
