
def getMinSpacesInPi(pi, favList):
    cache = {}
    numberTable = {num: True for num in favList}
    for i in (reversed(range(len(pi)))):
        getMinSpacesInPiFrom(i, pi, favList, cache, len(pi), numberTable)

    return -1 if cache[0] == float('inf') else cache[0]


def getMinSpacesInPiFrom(idx, pi, favList, cache, lastIdx, numberTable):
    if idx == lastIdx:
        return -1
    if idx in cache:
        return cache[idx]
    minSpace = float('inf')
    # '3141592', ['3141', '5', '31', '2', '4159', '9', '42']
    #
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in numberTable:
            minSpace = min(1 + getMinSpacesInPiFrom(i + 1, pi,
                                                    favList, cache, lastIdx, numberTable), minSpace)
    cache[idx] = minSpace
    print(cache)
    return cache[idx]


tc = ('3141592', ['3141', '5', '31', '2', '4159', '9', '42'])
pi = tc[0]
favList = tc[1]
print(getMinSpacesInPi(pi, favList))
