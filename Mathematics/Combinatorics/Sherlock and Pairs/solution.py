from collections import Counter

for _ in xrange(input()):
    input()    
    print reduce((lambda x,y: x + (y*(y-1))) , Counter(raw_input().split()).values(), 0)    
