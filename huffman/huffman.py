#!/usr/bin/env python

from Tree import Node, Leaf

class Huffman():

    def __init__(self, freq_map):
        self._freq_map = freq_map
        self._dataset = ''.join([ char[0] for char in freq_map ])
        self._tree = self._make_tree()
        self._code = self._code_map(self._tree, self._freq_map)

    def _make_tree(self):
        symbols = []
        for item in self._freq_map:
            symbols.append(Leaf(item[0], item[1]))
        for i in range(len(self._freq_map)):
            symbols = sorted(symbols, key=lambda symbols: symbols.weight)
            symbol_to_add=Node(symbols[1].value + symbols[0].value,
                                symbols[1].weight + symbols[0].weight, symbols[1], symbols[0])
            if len(symbols) == 2:
                return symbol_to_add
            symbols = [symbol_to_add] + symbols[2:]

    def _code_char(self, tree, char, code = ''):
        if tree.value == char:
            return code
        if char in tree.left.value:
            return self._code_char(tree.left, char, code + '1')
        elif char in tree.right.value:
            return self._code_char(tree.right, char, code + '0')

    def _code_map(self, tree, freq_map):
        result = {}
        for char in self._freq_map:
            result[char[0]] = self._code_char(tree, char[0])
        return result

    def encode(self, message):
        result = ''
        for char in message:
            if char in self._dataset:
                result += self._code[char]
        return result

    def _decode_char(self, message, tree, code = ''):
        if len(tree.value) == 1:
            return message, code + tree.value
        for bit in message:
            if bit == '1':
                return self._decode_char(message[1:], tree.left, code)
            elif bit == '0':
                return self._decode_char(message[1:], tree.right, code)

    def decode(self, message):
        result = ''
        while len(message) > 0:
            message, char  = self._decode_char(message, self._tree)
            result = result + char
        return result
