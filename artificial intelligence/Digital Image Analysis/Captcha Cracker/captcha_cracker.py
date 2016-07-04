
import md5

def getHash(charImg):
    m = md5.new()
    assert len(charImg) == 30*9
    for i in range(0, len(charImg)):
        b, g, r = charImg[i]
        b, g, r = int(b), int(g), int(r)
        if (b < 100) and (g < 100) and (r < 100):   # fuzzy match
            m.update(str(i))

    return m.hexdigest()


def recognize():
    char_map = {
    'e36e98f69fa1e34cdf9d42224edc37ca': '6',
    'ad6121e107c861597d888d8b84bd74ad': '0',
    'f04d3591a2f0d965f1d637c88d0cc646': '9',
    '9f30ef227a66fd196bd66db7036b0b28': '2',
    'b0d3f8cd8e7e17cf932d558bb5cb97ee': 'P',
    '0de8773a11915667a64478888da2315c': 'E',
    '0998e650310f923955ef6ecf4c5f9958': 'S',
    '4d6d892816f29784b07dc91fa04eb8df': 'T',
    'baa16c1cfc1c3bbf66dc63e950e07b1e': 'W',
    '38bf30f53237ebfd0c6df1b1eabe8f04': 'H',
    '0cc5932ac6a14bf86eb610f6d644f414': '1',
    '2ea9e830342ad8561caa2d9bba694356': 'L',
    '3e9711ce798dfe7fcc6db6987d75021d': 'D',
    'db9758594b7dc81bbea3edb2ba533437': 'R',
    'a32145a6238f4669b70d53182049cd42': '8',
    'd52813e86cd2e8b467c938e3a4761a09': '4',
    'b7461fffabf9926892a859ff08e83092': 'Z',
    '25b1696b315e018429488574ed2040c9': '7',
    'b1050141a9c77c444eeedd1a789a89db': 'Q',
    '55745f1f3fbc25c177fe96ece2e0870b': 'B',
    'ed5f9b7f915819474ce28307ef392bfc': 'F',
    'a91dd33b6d491a1e017196f1c9b07858': 'A',
    '97b35388eec42d386c282ca88e397b9f': 'M',
    '8452ebf5938cb82e7cafb358e7cb4b18': 'N',
    '12ab04ff9ba2c536016cf9f4f7678d71': 'J',
    'ffec35a7d46b15b1514a49003346fc19': 'K',
    '63e08116bd9a200c518aa58aee0acc69': 'V',
    '6c83e3bef1874876bddab0f13fdb60ff': 'U',
    'd4cdd084b0dfee466e200c15aad23eae': 'O',
    '519dad3edb3d125368dca7da2a4b3e3a': 'Y',
    '77abb42f05578099fa25a7bd1af14eb1': 'G',
    '476250f9416a27b5c457553f61da22f7': '5',
    'f6fe617c533be69a9499ec9ea8cd0745': 'C',
    'd28e7c57bace9e9c05dc11abeb1c1fd5': '3',
    '6ccf11383b9f1922c0b4c01e2415eb05': 'X',
    '07bba5063fc791b20a15c80974d47343': 'I'}
    #f = open('input24.txt')
    #rows, columns = f.readline().strip().split(' ')
    rows, columns = raw_input().split(' ')
    rows, columns = int(rows), int(columns)
    assert rows == 30
    assert columns == 60
    char1, char2, char3, char4, char5 = [], [], [], [], []

    for i in range(0, rows):
        #bgrList = f.readline().strip().split(' ')
        bgrList = raw_input().split(' ')
        assert len(bgrList) == 60

        for x in range(4, 4+9):
            b, g, r = bgrList[x].split(',')
            char1.append((b, g, r))

        for x in range(13, 13+9):
            b, g, r = bgrList[x].split(',')
            char2.append((b, g, r))

        for x in range(22, 22+9):
            b, g, r = bgrList[x].split(',')
            char3.append((b, g, r))

        for x in range(31, 31+9):
            b, g, r = bgrList[x].split(',')
            char4.append((b, g, r))

        for x in range(40, 40+9):
            b, g, r = bgrList[x].split(',')
            char5.append((b, g, r))

    #f.close()
    h1, h2, h3, h4, h5 = getHash(char1), getHash(char2), getHash(char3), getHash(char4), getHash(char5)
    output = '%s%s%s%s%s' %(char_map.get(h1), char_map.get(h2), char_map.get(h3), char_map.get(h4), char_map.get(h5))
    print output

def learn():
    def checkUnique(c, h, d):
        if h not in d:
            d[h] = c
        else:
            assert d[h] == c

    char_map = dict()
    # open all files
    for i in range(0, 24+1):
        inp = open('input%02d.txt' %(i))
        out = open('output%02d.txt' %(i))

        ol = out.readline().strip()
        out.close()

        c1, c2, c3, c4, c5 = ol[0], ol[1], ol[2], ol[3], ol[4],

        rows, columns = (inp.readline().strip()).split(' ')
        rows, columns = int(rows), int(columns)
        assert rows == 30
        assert columns == 60

        char1, char2, char3, char4, char5 = [], [], [], [], []

        for i in range(0, rows):
            bgrList = (inp.readline().strip()).split(' ')
            assert len(bgrList) == 60

            for x in range(4, 4+9):
                b, g, r = bgrList[x].split(',')
                char1.append((b, g, r))

            for x in range(13, 13+9):
                b, g, r = bgrList[x].split(',')
                char2.append((b, g, r))

            for x in range(22, 22+9):
                b, g, r = bgrList[x].split(',')
                char3.append((b, g, r))

            for x in range(31, 31+9):
                b, g, r = bgrList[x].split(',')
                char4.append((b, g, r))

            for x in range(40, 40+9):
                b, g, r = bgrList[x].split(',')
                char5.append((b, g, r))

        inp.close()
        h1, h2, h3, h4, h5 = getHash(char1), getHash(char2), getHash(char3), getHash(char4), getHash(char5)
        checkUnique(c1, h1, char_map)
        checkUnique(c2, h2, char_map)
        checkUnique(c3, h3, char_map)
        checkUnique(c4, h4, char_map)
        checkUnique(c5, h5, char_map)

    print char_map
    print len(char_map)

#learn()
recognize()