#!/usr/bin/env python
# coding=utf-8


class FL(object):

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def head(self):
        return self.values[0]

    def tail(self):
        return self.values[1:]

    def init(self):
        return self.values[:-1]

    def last(self):
        if self.values:
            return self.values[-1]
        else:
            return None

    def drop(self, n):
        return self.values[n:]

    def take(self, n):
        return self.values[:n]
