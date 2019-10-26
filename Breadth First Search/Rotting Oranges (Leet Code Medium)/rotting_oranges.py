def isInBounds(row, col, lastRow, lastCol):
    return not (row < 0 or col < 0 or row > lastRow or col > lastCol)


def countMinutes(grid):
    # We have to use bfs then only we will be able to solve
    # since the case 2100112 in the example both the sides start to rot at the same time
    # and thus we cannot manually do it one by one
    queue = []

    # add all the rotted oranges into the queue
    row = 0
    col = 0
    lastRow = len(grid) - 1
    lastCol = len(grid[0]) - 1

    # created a boolean visited matrix to keep track of the visited oranges
    visited = [[False for x in range(lastCol + 1)]
               for y in range(lastRow + 1)]

    for i in range(lastRow + 1):
        for j in range(lastCol + 1):
            if grid[i][j] == 2:  # it is rotten
                # 0 -> is the current minute or the base case
                queue.append([2, [i, j], 0])
                visited[i][j] = True
    print(queue)
    curMinute = 0
    minutes = 0
    # we iterate until the queue is again empty
    while len(queue) > 0:
        obj = queue.pop(0)
        curRow, curCol = obj[1]
        curMinute = obj[2]
        minutes = max(minutes, curMinute)
        # left
        if isInBounds(curRow - 1, curCol, lastRow, lastCol) and not visited[curRow - 1][curCol] and grid[curRow - 1][curCol] == 1:
            grid[curRow - 1][curCol] = 2
            visited[curRow - 1][curCol] = True
            queue.append([2, [curRow - 1, curCol], curMinute + 1])
        # [[1,1,2,0,2,0]]

        # right
        if isInBounds(curRow + 1, curCol, lastRow, lastCol) and not visited[curRow + 1][curCol] and grid[curRow + 1][curCol] == 1:
            grid[curRow + 1][curCol] = 2
            visited[curRow + 1][curCol] = True
            queue.append([2, [curRow + 1, curCol], curMinute + 1])

        # bottom
        if isInBounds(curRow, curCol - 1, lastRow, lastCol) and not visited[curRow][curCol - 1] and grid[curRow][curCol - 1] == 1:
            grid[curRow][curCol - 1] = 2
            visited[curRow][curCol - 1] = True
            queue.append([2, [curRow, curCol - 1], curMinute + 1])

        # up
        if isInBounds(curRow, curCol + 1, lastRow, lastCol) and not visited[curRow][curCol + 1] and grid[curRow][curCol + 1] == 1:
            grid[curRow][curCol + 1] = 2
            visited[curRow][curCol + 1] = True
            queue.append([2, [curRow, curCol + 1], curMinute + 1])

        # curMinute += 1

        # o/p 2
    # if there is a fresh orange left then we return -1
    for row in range(lastRow + 1):
        for col in range(lastCol + 1):
            if grid[row][col] == 1:
                return -1

    return minutes


tc1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
tc2 = [[1, 1, 2, 0, 2, 0]]
tc3 = [[0, 2]]
tc4 = [[1], [2]]
print(countMinutes(tc2))
print(countMinutes(tc1))
print(countMinutes(tc3))
print(countMinutes(tc4))
