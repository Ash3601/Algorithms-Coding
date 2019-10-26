# def multiStringSearch(smallStrings, bigString):
#     return [isInBigString(smallString, bigString) for smallString in smallStrings]


# def isInBigString(smallString, bigString):
#     for i in range(len(bigString)):
#         if i + len(smallString) > len(bigString):
#             break
#         if isInBigStringHelper(smallString, bigString, i):
#             return True

#     return False


# def isInBigStringHelper(smallString, bigString, startIdx):
#     leftSmallString = 0
#     rightSmallString = len(smallString) - 1
#     leftBigString = startIdx
#     rightBigString = startIdx + len(smallString) - 1

#     while leftBigString <= rightBigString:
#         if smallString[leftSmallString] != bigString[leftBigString] or smallString[rightSmallString] != bigString[rightBigString]:
#             return False

#         leftSmallString += 1
#         rightSmallString -= 1
#         leftBigString += 1
#         rightBigString -= 1
#     return True


# print(multiStringSearch([
#     "search", "me", "is", "a", "string"], "This is a big string"))

class Trie:
    def __init__(self):
        self.endSymbol = "*"
        self.root = {}

    def insertTrie(self, string):
        node = self.root
        for i in range(len(string)):
            currentLetter = string[i]
            if currentLetter not in node:
                node[currentLetter] = {}
            node = node[currentLetter]
        node[self.endSymbol] = string


def multiStringSearch(smallStrings, bigString):
    trie = Trie()
    for smallString in smallStrings:
        trie.insertTrie(smallString)

    containedString = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedString)

    return [smallString in containedString for smallString in smallStrings]


def findSmallStringsIn(string, startIdx, trie, containedString):
    currentNode = trie.root
    for i in range(startIdx, len(string)):
        letter = string[i]
        if letter not in currentNode:
            break
        currentNode = currentNode[letter]
        if trie.endSymbol in currentNode:
            containedString[currentNode[trie.endSymbol]] = True


class TrieModified:
    def __init__(self, string):
        self.root = {}
        self.buildTrie(string)

    def buildTrie(self, string):
        for i in range(len(string)):
            self.insertTrieAt(i, string)

    def insertTrieAt(self, startIdx, string):
        node = self.root
        for i in range(startIdx, len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
        return True


# trie = TrieModified("This is a big string")
# print(trie.root)
# def multiStringSearch(smallStrings, bigString):
#     trie = TrieModified(bigString)
#     return [trie.contains(smallString) for smallString in smallStrings]


print(multiStringSearch([
    "search", "me", "is", "a", "string", "this"], "This is a big string"))
