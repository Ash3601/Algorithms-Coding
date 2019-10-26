def isSafe(board, row, col):
    # Check the row for another queen
    for i in range(col):
        if board[row][i] == 1:
            return False  # Queen is present

    # We check in the diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col):
    N = len(board)
    if col >= N:
        return True

    # try placing queen in the rows considering the column one by one
    for i in range(N):
        if isSafe(board, i, col) == True:
            board[i][col] = 1  # place the queen

            # if the position turn out to be safe then return True
            if solveNQUtil(board, col + 1):
                return True

            # otherwise clear the board
            board[i][col] = 0

    return False


global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


solveNQ()
