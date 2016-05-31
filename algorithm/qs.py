#!/usr/bin/env python
# coding=utf-8


def bqs(l):
    less = []
    cl = []
    more = []

    if len(l) <= 1:
        return l
    else:
        c = l[0]
        for i in l:
            if i < c:
                less.append(i)
            elif i > c:
                more.append(i)
            else:
                cl.append(i)

        less = bqs(less)
        more = bqs(more)

        return less + cl + more


def qsort(l):
    return (qsort([y for y in l[1:] if y < l[0]]) + l[:1] + qsort([y for y in l[1:] if y >= l[0]])) if len(l) > 1 else l


qs = lambda xs: (
    (len(xs) <= 1 and[xs])
    or
    [qs([x for x in xs[1:] if x < xs[0]]) + [xs[0]] +
     qs([x for x in xs[1:] if x >= xs[0]])])[0]

if __name__ == '__main__':
    t = [4, 6, 8, 4, 23, 2]
    print qs(t)
    print qsort(t)

    print bqs(t)
