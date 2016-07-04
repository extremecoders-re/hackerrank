# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

T = input()
for i in range(0, T):
    l = raw_input().split()
    low = int(l[0])
    high = int(l[1])
    print int(math.floor(math.sqrt(high)) - math.ceil(math.sqrt(low))) + 1