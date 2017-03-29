from operator import xor

input()
print reduce(xor, map(int,raw_input().strip().split(' ')))
