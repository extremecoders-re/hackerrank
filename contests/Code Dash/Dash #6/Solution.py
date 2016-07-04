#!/bin/python
def partition(ar):
    p = ar[0]
    less ,more = [], []
    for i in range(1, len(ar)):
        el = ar[i]
        if el < p:
            less.append(el)
        elif el > p:
            more.append(el)
    less.append(p)
    for el in more:
        less.append(el)
    for el in less:
        print el,

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)