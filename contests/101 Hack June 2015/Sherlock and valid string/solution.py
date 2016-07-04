import sys
S = raw_input()
freq = [0 for i in range(0,26)]

for ch in S:
    freq[ord(ch) - 97] += 1

# Remove all zero occurences
freq = filter(lambda a: a > 0, freq)

if freq.count(freq[0]) == len(freq): # Already valid
    print 'YES'
    sys.exit()

freq_copy = freq[:]

for i in range(0, len(freq_copy)):
    freq = freq_copy[:]
    freq[i] -= 1
    freq = filter(lambda a: a > 0, freq)
    if freq.count(freq[0]) == len(freq):
        print 'YES'
        sys.exit()

print 'NO'