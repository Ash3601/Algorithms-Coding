class TrieNode:
    def __init__(self):
        self.charArr = [None] * 26
        self.word = None
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, chars):
        curNode = self.root
        for i in range(len(chars)):
            idx = int(ord(chars[i]) - ord('a'))
            if curNode.charArr[idx] == None:
                curNode.charArr[idx] = TrieNode()
            curNode = curNode.charArr[idx]
        # make the word
        curNode.isWord = True
        curNode.word = chars

    def search(self, stringToSearch):
        currentNode = self.root
        for i in range(len(stringToSearch)):
            idx = int(ord(stringToSearch[i]) - ord('a'))
            if currentNode.charArr[idx] == None:
                return False
            currentNode = currentNode.charArr[idx]
        return currentNode is not None and currentNode.isWord


def searchInBoard(board, stringsToSearch):
    trie = Trie()
    root = trie.root
    for word in stringsToSearch:
        trie.insert(word)
    # print(trie.search("eat"))
    # create a result set
    res = []

    rows = len(board[0])
    cols = len(board)

    # iterate over the board
    for r in range(rows):
        for c in range(cols):
            currentChar = board[r][c]
            if root.charArr[ord(currentChar) - ord('a')] is not None:
                dfs(board, r, c, res, root, currentChar, rows, cols)
    return res

# check if the point is in bounds


def isOutOfBounds(r, c, rows, cols):
    if r < 0 or c < 0:
        return True
    if r >= rows or c >= cols:
        return True
    return False


def dfs(board, r, c, res, root, char, rows, cols):
    if visited[r][c] == True or root.charArr[ord(char) - ord('a')] is None:
        return
    visited[r][c] = True
    currentChar = board[r][c]
    root = root.charArr[ord(currentChar) - ord('a')]
    # print("Root is ", root.word)
    if root != None and root.isWord:
        # print('In appending')
        res.append(root.word)
    for k in range(len(dr)):
        row = r + dr[k]
        col = c + dc[k]
        if isOutOfBounds(row, col, rows, cols):
            continue
        dfs(board, row, col, res, root, board[row][col], rows, cols)
    visited[r][c] = False


matrix = [
    list("oaan"),
    list("etae"),
    list("ihkr"),
    list("iflv")
]
visited = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]
# l # r # b # t
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

input1 = ["oath", "eat", "oat", "pak"]

# print(matrix)
# print(visited)
# trie = Trie()
# chars = "string"
# trie.insert(chars)
# print(trie.root.charArr)
# print(trie.search(chars))
ans = searchInBoard(matrix, input1)
print("Following Strings found ", end=" ")
print(ans)
