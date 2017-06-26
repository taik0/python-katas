#!/usr/bin/env python

from gen_freq_map import gen_freq_map
from huffman import Huffman

f = open('dqdlm.txt', 'rb')
freq_map = gen_freq_map(f.read())
x = Huffman(freq_map)
t = open('dqdlm.txt', 'rb')

msg = x.encode(t.read())

print "Msg len: ", len(msg)
print "Msg in MB: ", len(msg)/(8.0*1024**2)
