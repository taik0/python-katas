#!/usr/bin/env python

from gen_freq_map import gen_freq_map
from huffman import Huffman

dataset = 'abcdefghijklmnopqrstuvwxyz'
#dataset = 'abcdef'
f = open('sample.txt', 'r')
freq_map = gen_freq_map(dataset, f.read())


x = Huffman(freq_map)

msg = x.encode('hola que tal! como te va')
print "encode msg: ", msg
print x.decode(msg)
