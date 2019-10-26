matrix = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


printMatrix(matrix)


def zig_zag_traversal(matrix):
    lastRow = len(matrix) - 1
    lastCol = len(matrix[0]) - 1
    print("Last Row ", lastRow, "Last Col", lastCol)
    row = 0
    col = 0
    goingDown = True
    result = []
    while not isOutOfBounds(row, col, lastCol, lastRow):
        result.append(matrix[row][col])
        print("Current Row", row, "Current Col", col)
        if goingDown:
            if col == 0 or row == lastRow:
                goingDown = False
                if row == lastRow:
                    col = col + 1
                else:
                    row = row + 1
            else:
                row += 1
                col -= 1
        else:
            if col == lastCol or row == 0:
                goingDown = True
                if col == lastCol:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


def isOutOfBounds(row, col, lastCol, lastRow):
    return row > lastRow or col > lastCol or row < 0 or col < 0


result = zig_zag_traversal(matrix)
print(result)
