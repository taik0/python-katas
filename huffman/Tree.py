#!/usr/bin/env python

class Node(object):

    def __init__(self, value, weight, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.weight = weight

    def _code_char(self, char, code = ''):
        if char in self.left.value:
            return self.left._code_char(char, code + '1')
        elif char in self.right.value:
            return self.right._code_char(char, code + '0')

    def _decode_char(self, message):
        if len(self.value) == 1:
            return message, self.value
        for bit in message:
            if bit == '1':
                return self.left._decode_char(message[1:])
            elif bit == '0':
                return self.right._decode_char(message[1:])

class Leaf(object):

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def _code_char(self, char, code = ''):
        if char == self.value:
            return code

    def _decode_char(self, message):
        return message, self.value
