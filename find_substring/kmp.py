#!/usr/bin/env python
"""
https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
Knuth–Morris–Pratt string searching algorithm (or KMP algorithm) searches for
occurrences of a "word" W within a main "text string" S by employing the
observation that when a mismatch occurs, the word itself embodies sufficient
information to determine where the next match could begin, thus bypassing
re-examination of previously matched characters.
"""

def table(needle):
    """
    The complexity of the table algorithm is O(k), where k is the length of needle.
    """
    pos = 1
    cnd = 0
    symbol_table = [0 for i in range(len(needle))]
    symbol_table[0] = -1
    while pos < len(needle):
        if needle[pos] == needle[cnd]:
            symbol_table[pos] = symbol_table[cnd]
            pos += 1
            cnd += 1
        else:
            symbol_table[pos] = cnd
            cnd = symbol_table[cnd]
            while cnd >= 0 and needle[pos] != needle[cnd]:
                cnd = symbol_table[cnd]
            pos += 1
            cnd += 1
    return symbol_table

def search(needle_str, text_str):
    """
    The complexity for the search ins O(n) where n is the length of text_str.
    """
    needle = str.encode(needle_str)
    text = str.encode(text_str)
    symbol_table = table(needle)
    j = 0
    k = 0
    while j < len(text):
        if needle[k] == text[j]:
            j += 1
            k += 1
            if k == len(needle):
                return j - k
        else:
            k = symbol_table[k]
            if k < 0:
                j += 1
                k += 1
    return -1

s1 = "bah"
s2 = "Hello how are you"

print(search(s1, s2))

print(search("ais", "aaaaaaaaaaaisbaababba"))
