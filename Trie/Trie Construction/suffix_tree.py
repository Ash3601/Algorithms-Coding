class SuffixTree:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        currentNode = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in currentNode:
                currentNode[letter] = {}
            currentNode = currentNode[letter]
        currentNode[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:  # if the string is not matched
                return False
            node = node[letter]  # if matching then move to the next node.
        # if we never hit the False condition then
        return self.endSymbol in node


suffixTrie = SuffixTree('babc')
print(suffixTrie.contains('ba'))
