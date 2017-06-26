#!/usr/bin/env python

from operator import itemgetter

def gen_freq_map(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return sort_freq_map(result)

def sort_freq_map(freq_map):
    return sorted(freq_map.items(), key=itemgetter(1))
