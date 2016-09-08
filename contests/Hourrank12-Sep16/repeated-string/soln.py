s = raw_input().strip()
n = long(raw_input().strip())
print s.count('a')*(n/len(s))+s[0:n%len(s)].count('a')
