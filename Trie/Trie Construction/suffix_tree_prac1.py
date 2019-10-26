class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.buildSuffixTrie(string)

    def buildSuffixTrie(self, string):
        for i in range(len(string)):
            self.buildSuffixFromStringFrom(i, string)

    def buildSuffixFromStringFrom(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            if string[j] not in node:
                node[string[j]] = {}
            node = node[string[j]]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


sft = SuffixTrie('baccb')
print(sft.contains('ba'))
