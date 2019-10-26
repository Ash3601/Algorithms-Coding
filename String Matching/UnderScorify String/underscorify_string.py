def underScorify(string, match):
    # test
    # testthis is a testtest
    # 1. find the index of the matching tests
    i = 0
    matchedIndices = []
    while i < len(string):
        matchedIndex = findIndexOfMatchedStringFrom(i, string, match)
        if matchedIndex is not None:
            matchedIndices.append(matchedIndex)
            i = matchedIndex[1] - 1
        else:
            i += 1
    print(matchedIndices)

    # 2. collapse the ranges
    collapsedIndices = []
    collapsedIndices = getCollapsedIndicesFrom(
        matchedIndices, collapsedIndices)
    print("Collapsed Indices are", collapsedIndices)

    # 3. underscorify
    underScorifiedString = getUnderScorifiedStringFrom(
        collapsedIndices, string)

    print(underScorifiedString)


def getUnderScorifiedStringFrom(indices, string):
    # for idx1, idx2 in ind/ices:
        # string = string[:i/dx/1 + 1] + "_" + string[idx1:]

    stringList = list(string)
    inserted = 0
    for idx1, idx2 in indices:
        stringList.insert(idx1 + inserted, '_')
        stringList.insert(idx2 + 1 + inserted, '_')
        inserted += 2
    return ''.join(stringList)


def getCollapsedIndicesFrom(indices, collapsedIndices):
    n = len(indices)
    i = 1
    if n == 1:
        return indices
    collapsedIndices.append(indices[0])
    print(collapsedIndices)
    while i < n:
        if indices[i][0] <= collapsedIndices[-1][1]:
            collapsedIndices[-1][1] = indices[i][1]
            # collapsedIndices.append(
            # [collapsedIndices[i - 1][0], indices[i][1]])
            # del indices[i-1]
            # n -= 1
        else:
            collapsedIndices.append(indices[i])
        i += 1
    # if indices[-1][0] > indices[-2][1]:
    #     collapsedIndices.append(indices[-1])
    # elif indices[-1][0] <= indices[-2][1]:
    #     #! TODO Collapse the last indices with previous one and append
    #     collapsedIndices.append((indices[-2][0], indices[-1][1]))
    #     del indices[-1]
    #     n -= 1

    return collapsedIndices


def getCollapsedIndicesFrom2(indices, collapsedIndices):
    n = len(indices)
    i = 1
    if n == 1:
        return indices
    while i < n:
        if indices[i][0] <= indices[i - 1][1]:
            collapsedIndices.append((indices[i - 1][0], indices[i][1]))
            del indices[i - 1]
            n -= 1
        else:
            collapsedIndices.append(indices[i-1])
        i += 1
    if indices[-1][0] > indices[-2][1]:
        collapsedIndices.append(indices[-1])
    elif indices[-1][0] <= indices[-2][1]:
        #! TODO Collapse the last indices with previous one and append
        collapsedIndices.append((indices[-2][0], indices[-1][1]))
        del indices[-1]
        n -= 1

    return collapsedIndices


def findIndexOfMatchedStringFrom(startIdx, string, match):
    for i in range(0, len(match)):
        if startIdx + i < len(string) and string[startIdx + i] == match[i]:
            if i == len(match) - 1:
                return list(reversed([startIdx + i + 1, startIdx + i - len(match) + 1]))
            i += 1
        else:
            break
    return None


string = "testthis is a testtest to see testestest it works"
match = "this"
underScorify(string, match)
