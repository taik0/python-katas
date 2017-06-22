#!/usr/bin/env python

from Tree import Node, Leaf

class Huffman():

    def __init__(self, freq_map):
        self._freq_map = freq_map
        self._dataset = ''.join([ char[0] for char in freq_map ])
        self._tree = self._make_tree()

    def _make_tree(self):
        symbols = []
        for item in self._freq_map:
            symbols.append(Leaf(item[0], item[1]))
        for i in range(len(self._freq_map)):
            symbols = sorted(symbols, key=lambda symbol: symbol.weight)
            symbol_to_add=Node(symbols[1].value + symbols[0].value,
                                symbols[1].weight + symbols[0].weight, symbols[1], symbols[0])
            if len(symbols) == 2:
                return symbol_to_add
            symbols = [symbol_to_add] + symbols[2:]


    def encode(self, message):
        result = ''
        for char in message:
            if char in self._dataset:
                result += self._tree._code_char(char)
        return result


    def decode(self, message):
        result = ''
        while len(message) > 0:
            message, char  = self._tree._decode_char(message)
            result = result + char
        return result
