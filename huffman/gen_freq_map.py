#!/usr/bin/env python

from operator import itemgetter

def gen_freq_map(dataset, string):
    result = {}
    for i in dataset:
        result[i] = 0
    for char in string.lower():
        if char in dataset:
            result[char] += 1
    return sort_freq_map(result)

def sort_freq_map(freq_map):
    return sorted(freq_map.items(), key=itemgetter(1))
