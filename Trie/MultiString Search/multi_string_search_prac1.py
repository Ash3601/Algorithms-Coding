def multiStringSearch(stringToMatch, strings):
    i = 0
    for string in strings:
        i = 0
        j = 0
        while i < len(stringToMatch):
            if stringToMatch[i] == string[j]:
                print("Matching", i, j)
                if j == len(string) - 1:
                    print("String found is ", string)
                    break
                i += 1
                j += 1
            else:
                i += 1
                j = 0


class Trie:
    def __init__(self):
        self.endSymbol = "*"
        self.root = {}

    def insert(self, string):
        curNode = self.root
        for i in range(len(string)):
            if string[i] not in curNode:
                curNode[string[i]] = {}
            curNode = curNode[string[i]]
        curNode[self.endSymbol] = string


def multiStringSearchTrie(stringToMatch, strings):
    # Build Trie
    trie = Trie()
    for string in strings:
        trie.insert(string)
    # now trie is complete
    containedString = {}
    for idx in range(len(stringToMatch)):
        findSmallStringsIn(stringToMatch, strings, trie, idx, containedString)

    print(containedString)


def findSmallStringsIn(bigString, smallStrings, trie, idx, containedString):
    currentNode = trie.root
    for i in range(idx, len(bigString)):
        if bigString[i] not in currentNode:
            break
        currentNode = currentNode[bigString[i]]
    if '*' in currentNode:
        print("String found", currentNode['*'])
        containedString[currentNode['*']] = True


trie = Trie()
trie.insert("this")
trie.insert("is")
trie.insert("thanos")
print(trie.root)

strings = ["this", "is", "am"]
stringToMatch = "this is am"
multiStringSearchTrie(stringToMatch, strings)
# multiStringSearch(stringToMatch, strings)
