# Find substrings in strings

I was asked how to find a substring in a string in an interview a I didn't know
the existence of `str.find()` so I digged into string search algorithms.

## Boyer-Moore-Horspool algorithm

[Boyer-Moore-Horspool](https://en.wikipedia.org/wiki/Boyer-Moore-Horspool_algorithm)
It is a simplification of the Boyer–Moore string search algorithm which is related to the Knuth–Morris–Pratt algorithm. The algorithm trades space for time in order to obtain an average-case complexity of O(n) on random text, although it has O(nm) in the worst case, where the length of the pattern is m and the length of the search string is n.

## Knuth–Morris–Pratt algorithm

[Knuth–Morris–Pratt](https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm)
Knuth–Morris–Pratt string searching algorithm (or KMP algorithm) searches foroccurrences of a "word" W within a main "text string" S by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.
