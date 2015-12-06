#!/usr/bin/env python
# coding=utf-8


class Stack(object):

    def __init__(self, size=0):
        self.stack = []
        self.size = size

    def _is_empty(self):
        return len(self.stack) == 0

    def _is_full(self):
        return len(self.stack) == self.size

    def push(self, element):
        if self._is_full():
            raise Exception('stack full')
            # return
        else:
            self.stack.append(element)

    def pop(self):
        if self._is_empty():
            raise Exception('stack empty')
        else:
            self.stack.pop()
