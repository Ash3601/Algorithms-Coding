def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]


def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break

        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False


def isInBigStringHelper(bigString, smallString, startIdx):
    smallLeftIdx = 0
    smallRightIdx = len(smallString) - 1
    bigLeftIdx = startIdx
    bigRightIdx = len(smallString) - 1 + startIdx

    while bigLeftIdx <= bigRightIdx:
        if bigString[bigLeftIdx] != smallString[smallLeftIdx] or bigString[bigRightIdx] != smallString[smallRightIdx]:
            return False
        smallLeftIdx += 1
        smallRightIdx -= 1
        bigLeftIdx += 1
        bigRightIdx -= 1

    return True


class TrieModified:
    def __init__(self, string):
        self.root = {}
        self.buildTrie(string)

    def buildTrie(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                pass


print(multiStringSearch("this is a string",
                        ["this", "a", "yo", "str", " a str"]))
