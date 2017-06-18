#!/usr/bin/env python

# Pruebas a mano

import itertools

dataset = [''.join(x) for x in itertools.product('abcdefghij', repeat=4)]
dataset2 = [''.join(x) for x in itertools.product('klmnopqrst', repeat=4)]

dataset += dataset2

data = []
for i in range(1000000):
    if i % 2 == 0:
        data.append(str(i))

from set_05 import Bloomfilter
from set_04 import Hashedbitset

setx = Bloomfilter(43132763, 30)
#setx = Kset()
#setx = Hashedbitset(500000)
for t in data:
    setx.Add(t)
print "Dataset size: ", len(dataset)
print "Set contains unknown string: ", setx.Contains('17')
print "Set contains unknown string: ", setx.Contains('555221')
print "Set contains known string: ", setx.Contains('2')
print "Set contains known string: ", setx.Contains('999998')
print "Set contains known string: ", setx.Contains('8888')
print "Set contains known string: ", setx.Contains('55556')
