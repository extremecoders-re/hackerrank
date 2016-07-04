N, P, X = raw_input().split()
N, P, X = int(N), int(P), int(X)

line = raw_input()

max_rating = 0
cand_id = 0
i = 0

for s in line.split():
    score = int(s)
    rating = score * P
    P -= X
    i += 1
    if rating >= max_rating:
        max_rating = rating
        cand_id = i
        
print cand_id