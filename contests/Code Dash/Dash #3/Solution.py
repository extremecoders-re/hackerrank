# Enter your code here. Read input from STDIN. Print output to STDOUT

T = input()
for i in range(0, T):
    n, a, b = input(), input(), input(),
    values = [0]
    stoneNum = 1
    while stoneNum < n:
        temp = []
        for v in values:
            x = v + a
            if x not in temp:
                temp.append(x)
            x = v + b
            if x not in temp:
                temp.append(x)
        stoneNum += 1
        values = temp

    values.sort()
    for v in values:
        print v,
    print