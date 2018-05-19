#!/usr/bin/env python
"""
The algorithm trades space for time in order to obtain an average-case
complexity of O(n) on random text, although it has O(nm) in the worst case,
where the length of the pattern is m and the length of the search string is n.
"""

def preprocess(pattern):
    """
    Preprocesses the pattern to produce a table containing, for each symbol in
    the alphabet, the number of characters that can safely be skipped.
    """
    symbol_table = [len(pattern) for i in range(256)]
    for i in range(len(pattern) - 1):
        symbol_table[pattern[i]] = len(pattern) -1 -i
    return symbol_table

def search(needle_str, haystack_str):
    """
    search reports the index of the first occurrence of needle in haystack.
    We must encode the strings to bytes.
    """
    needle = str.encode(needle_str)
    haystack = str.encode(haystack_str)
    symbol_table = preprocess(needle)
    skip = 0
    while len(haystack) - skip >= len(needle):
        i = len(needle) -1
        while haystack[skip + i] == needle[i]:
            if i == 0:
                return skip
            i -= 1
        skip += symbol_table[haystack[skip + len(needle) -1]]
    return -1

print(search("how", "Hello how are you"))

print(search("ais", "aaaaaaaaaaaisbaababba"))
