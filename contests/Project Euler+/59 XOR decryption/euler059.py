# Sample Input
# 32 66 50 20 11 0 42 66 33 19 13 20 47 66 37 14 58 67 43 23 14 17 49 67 46 20 6 51 66 55 9 39 67 45 3 25 56 66 39 14 37 34 65 51 22 8 1 40 65 32 17 14 21 45 65 36 12 57 66 41 20 15 19 50 66 44 23 7 49 65 54 11 36 66 47 0 24 58 65 38 12 38

N = int(raw_input())
encrypted = raw_input().split(' ')
encrypted = map(int, encrypted)
chars_plaintext = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789();:,.'?-! "
possible_key1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
possible_key2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
possible_key3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = 0
while x < len(encrypted):
    if len(possible_key1) > 1:
        temp = []
        for k in possible_key1:
            if chr(ord(k) ^ encrypted[x]) in chars_plaintext:
                temp.append(k)
        possible_key1 = temp
    x += 1
    if x == len(encrypted):
        break

    if len(possible_key2) > 1:
        temp = []
        for k in possible_key2:
            if chr(ord(k) ^ encrypted[x]) in chars_plaintext:
                temp.append(k)
        possible_key2 = temp
    x += 1
    if x == len(encrypted):
        break

    if len(possible_key3) > 1:
        temp = []
        for k in possible_key3:
            if chr(ord(k) ^ encrypted[x]) in chars_plaintext:
                temp.append(k)
        possible_key3 = temp
    x += 1

print "%s%s%s" %(possible_key1[0], possible_key2[0], possible_key3[0])