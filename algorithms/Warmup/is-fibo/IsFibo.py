# Enter your code here. Read input from STDIN. Print output to STDOUT

def isFibo(num):
    n1 = 0
    n2 = 1
    s = 0
    while s < num:
        n1 = n2
        n2 = s
        s = n1 + n2
    if s == num:
        return True
    else:
        return False        
    

T = int(raw_input())

for i in range(0, T):
    num = int(raw_input())
    if isFibo(num):
        print "IsFibo"
    else:
        print "IsNotFibo"     