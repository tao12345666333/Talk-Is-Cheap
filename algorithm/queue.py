#!/usr/bin/env python
# coding=utf-8


class Queue(object):

    def __init__(self, size=0):
        self.size = size
        self.queue = []

    def _is_empty(self):
        return len(self.queue) == 0

    def _is_full(self):
        return len(self.queue == self.size)

    def enqueue(self, element):
        if self._is_full():
            raise Exception('queue is full')
        else:
            self.queue.append(element)

    def dequeue(self):
        if self._is_empty():
            raise Exception('queue is empty')
        else:
            self.queue.pop(0)


if __name__ == '__main__':
    queue = Queue()
