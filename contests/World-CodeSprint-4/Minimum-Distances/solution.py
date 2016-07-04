n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

minm = -1
for dist in xrange(1, n, 1):
    for i in xrange(n):
        if i + dist >= n:
            break
        if A[i] == A[i+dist]:
            if minm == -1:
                minm = dist
                
            elif dist < minm:
                minm = dist
                
print minm 
