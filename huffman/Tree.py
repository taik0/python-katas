#!/usr/bin/env python

class Node(object):

    def __init__(self, value, weight, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.weight = weight

    def _code_char(self, char, code = ''):
        if char in self.left.value:
            if len(self.left.value) == 1:
                return  code + '1'
            return self.left._code_char(char, code + '1')
        elif char in self.right.value:
            if len(self.right.value) == 1:
                return code + '0'
            return self.right._code_char(char, code + '0')

    def _decode_char(self, message):
        for bit in message:
            if bit == '1':
                if len(self.left.value) == 1:
                    return message[1:], self.left.value
                return self.left._decode_char(message[1:])
            elif bit == '0':
                if len(self.right.value) == 1:
                    return message[1:], self.right.value
                return self.right._decode_char(message[1:])

class Leaf(object):

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
