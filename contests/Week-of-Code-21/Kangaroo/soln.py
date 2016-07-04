x1,v1,x2,v2 = map(int, raw_input().strip().split(' '))

if v1 == v2:
    print 'NO'

else:
    res = float(x1 - x2) / float(v2 - v1)
    if res >= 0 and res.is_integer():
        print 'YES'
    else:
        print 'NO
