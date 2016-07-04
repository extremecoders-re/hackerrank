n1, n2, n3 = map(int, raw_input().split(' '))
s1, s2, s3 = [map(int, raw_input().split(' '))[::-1] for i in range(3)]

sum_s1, sum_s2, sum_s3 = sum(s1), sum(s2), sum(s3)

while not sum_s1 == sum_s2 == sum_s3:
    maxval = max(sum_s1, sum_s2, sum_s3)
    if sum_s1 == maxval:
        sum_s1 -= s1.pop()
    elif sum_s2 == maxval:
        sum_s2 -= s2.pop()
    else:
        sum_s3 -= s3.pop()
    
print sum_s1
