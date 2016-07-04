N = input()
avail_facil = [raw_input().strip() for i in range(N)]
descrip = raw_input().strip().lower()

found = []
for f in avail_facil:
    if f.lower() in descrip:
        found.append(f)
        
found.sort()
for f in found:
    print f