global N
N = 20


def isSafe(board, row, col):
    # check for row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check the lower diagonal'
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check the upper diagonal'
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def NQueensHelper(board, col):
    N = len(board)

    if col >= N:
        return True  # we are done

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if NQueensHelper(board, col+1):
                return True

        board[i][col] = 0

    return False


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def solveNQ():
    board = [[0 for i in range(N)] for j in range(N)]

    if NQueensHelper(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


solveNQ()
