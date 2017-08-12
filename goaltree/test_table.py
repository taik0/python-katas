#!/usr/bin/env python

import unittest
from table import Table
from block import Block

class TestTable(unittest.TestCase):

    def test_table_init(self):
        t = Table(2,10)
        self.assertEqual(t.height, 10)
        self.assertEqual(t.width, 2)

    def test_table_str(self):
        t = Table(3, 2)
        s = str(t)
        self.assertEqual(s, 'None\tNone\tNone\nNone\tNone\tNone')

    def test_is_valid(self):
        t = Table(5,2)
        self.assertFalse(t._is_valid(0,-1))
        self.assertFalse(t._is_valid(-1,0))
        self.assertFalse(t._is_valid(5,0))
        self.assertFalse(t._is_valid(0,2))
        self.assertTrue(t._is_valid(3,0))
        self.assertFalse(t._is_valid(0,2))
        self.assertTrue(t._is_valid(0,0))
        t.set(0,0, Block('TEST01'))
        self.assertFalse(t._is_valid(0,0))
        self.assertTrue(t._is_valid(0,1))

    def test_is_empty(self):
        t = Table(3,3)
        self.assertTrue(t.is_empty(0,0))
        t.set(0,0, Block('TEST01'))
        self.assertFalse(t.is_empty(0,0))
        self.assertTrue(t.is_empty(0,1))
        self.assertTrue(t.is_empty(1,0))

    def test_set(self):
        t = Table(10,5)
        self.assertRaises(AssertionError, t.set, 11,0, None)
        self.assertRaises(AssertionError, t.set, 0, 0, '')
        self.assertTrue(t.set(0,0,Block('0001')))
        self.assertTrue(t.set(0,1,Block('0002')))


    def test_get(self):
        t = Table(5,10)
        t.set(0,0,Block('000'))
        t.set(0,1,Block('001'))
        t.set(0,2,Block('002'))
        t.set(0,3,Block('003'))
        t.set(0,4,Block('004'))
        t.set(1,0,Block('005'))
        t.set(1,1,Block('006'))
        t.set(1,2,Block('007'))
        t.set(1,3,Block('008'))
        self.assertEqual(t.get('008').name, '008')
        self.assertEqual(t.get('XXX'), None)
        self.assertEqual(t.get('004').row, 4)
        self.assertEqual(t.get('004').col, 0)

    def test_next_empty(self):
        t = Table(4,5)
        t.set(0,0,Block('000'))
        t.set(0,1,Block('001'))
        t.set(0,2,Block('002'))
        t.set(0,3,Block('003'))
        t.set(0,4,Block('004'))
        t.set(1,0,Block('005'))
        t.set(1,1,Block('006'))
        t.set(1,2,Block('007'))
        t.set(1,3,Block('008'))
        self.assertEqual(t.next_empty(0), -1)
        self.assertEqual(t.next_empty(1), 4)
        t.set(1,4,Block('009'))
        self.assertEqual(t.next_empty(1), -1)
        self.assertEqual(t.next_empty(2), 0)
        t.set(2,0,Block('010'))
        self.assertEqual(t.next_empty(2), 1)



if __name__ == '__main__':
    unittest.main()
