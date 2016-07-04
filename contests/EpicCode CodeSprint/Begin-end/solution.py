N = input()
s = raw_input()

ans = N
freq = [0 for i in range(26)]

for i in range(0, N):
    freq[ord(s[i]) - 97] += 1
    
for i in range(0, 26):
    temp = freq[i]
    temp = (temp * (temp - 1)) >> 1
    ans += temp    
       
print ans