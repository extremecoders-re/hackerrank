def fuzzyMatch(pattern, target, numVars):
    '''
    @type pattern : list
    @type target : string
    Both pattern and target must be of same length
    '''
    #pattern = list()
    #target = str()

    # Check fixed letters
    for i in range(0, len(pattern)):
        val = pattern[i]
        if isinstance(val, str):
            if val != target[i]:
                return False

    for n in range(1, numVars + 1):
        sameCharPos = list()

        # First find the postion of same characters in pattern
        for i in range(0, len(pattern)):
            if pattern[i] == n:
                sameCharPos.append(i)

        # Now check if the characters are same in the target string
        ch = target[sameCharPos[0]]
        for i in range(0, len(sameCharPos)):
            if ch != target[sameCharPos[i]]:
                return False
    return True

def findAllPositions(ch, string):
    positions = list()
    for i in range(0, len(string)):
        if ch == string[i]:
            positions.append(i)
    return positions

def buildPattern(cipherText):
    global found_map
    numVars = 1
    checkedPositions = list()
    pattern = list(' ' * len(cipherText))   # Build empty pattern of strlen size

    for i in range(0, len(cipherText)):
        ch = cipherText[i]
        if found_map.has_key(ch):
            pattern[i] = found_map.get(ch)
        elif checkedPositions.count(i) == 0:
            positions = findAllPositions(ch, cipherText)
            # More than one position exists
            if len(positions) > 1:
                for p in positions:
                    pattern[p] = numVars
                    checkedPositions.append(p)
                numVars += 1
            else:
                pattern[i] = 0
    return pattern, numVars - 1

def putToDict(cipherText, plainText, d):
    for i in range(0, len(cipherText)):
        d[cipherText[i]] = plainText[i]

f = open('dictionary.lst')
dictWords = f.readlines()
f.close()

for i in range(0, len(dictWords)):
    dictWords[i] = dictWords[i].strip().lower()

found_map = dict()  # dictionary to hold already found cipher mapping
alreadyDecryptedWords = dict()   # dictionary to hold already decrypted words

# This is the input text, it contains space separated encrypted words
'''
fullText = 'lhpohes gvjhe ztytwojmmtel lgsfcgver segpsltjyl vftstelc djfl rml catrroel jscvjqjyfo mjlesl\
 lcjmmfqe egvj gsfyhtyq sjfgver csfaotyq lfxtyq gjywplesl lxljm dxcel mpyctyq ztytwojmmtelel mfcgv spres\
 mjm psgvty bfml ofle mjlc dtc tygfycfctjy dfsyl zpygvel csfao yealqsjpml atyl lgsjql qyfsotelc fseyf\
 ojllel gjzmselltyq wpyhtelc zpltgl weygel afyher rstnesl aefleo rtyhes mvflel yphe rstnes qojder dtwwer\
 lojml mfcgvel reocfl djzder djpygtyq gstmmoeafsel reg cpdel qspyqe mflctel csflvtyq vfcl avfghtyq vftsdfool\
 mzer sfmtyq rsjye wjjol psol mplvtyq catrroe mvfqe lgseey leqzeycer wjseqsjpyrer lmjtoes msjwtoel docl djpyger\
 cjpstlcl goefy gojddesl mjrl qjddoe gjy gpdtyql lyftotyq rjayojfr swgl vjle atrqec gjzmfgces frfl qotcgver gspzd zftodjzdl lyfsh'
'''

fullText = str(raw_input())
encWordList = fullText.split(' ')

# Assuming all words in encWordList are unique
while len(alreadyDecryptedWords) < len(encWordList):
    for i in range(0, len(encWordList)):
        cipherText = encWordList[i]
        matchesWordList = list()

        for word in dictWords:
            # Break if more than one match is found
            if len(matchesWordList) > 1:
                break
            if len(cipherText) == len(word):
                p, n = buildPattern(cipherText)
                if fuzzyMatch(p, word, n):
                    matchesWordList.append(word)

        # Now check if we have exact one fuzzy match
        if len(matchesWordList) == 1:
            putToDict(cipherText, matchesWordList[0], found_map)
            alreadyDecryptedWords[cipherText] = matchesWordList[0]

for word in encWordList:
    print alreadyDecryptedWords.get(word),