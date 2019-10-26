def riverLengths(matrix):
    # lets create an auxilliary matrix of booleans
    visited = [[False for i in range(len(matrix[0]))]
               for j in range(len(matrix))]

    sizes = []

    # iterate over the elements of the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]:
                continue
            traverseNeighbourNodes(i, j, matrix, sizes, visited)
    print(sorted(sizes))


def traverseNeighbourNodes(i, j, matrix, sizes, visited):
    queue = [[i, j]]  # append the root node

    currentRiverSizes = 0

    while len(queue):

        i, j = queue.pop(0)

        if visited[i][j]:
            continue

        visited[i][j] = True

        if matrix[i][j] == 0:
            continue

        # means at this point the node is surely gonna be 1
        currentRiverSizes += 1

        queue = checkNearNeighbours(i, j, matrix, visited)

    if currentRiverSizes > 0:
        sizes.append(currentRiverSizes)

    # print(visited)


def checkNearNeighbours(i, j, matrix, visited):

    unvisitedNeighbours = []

    # check the left
    if isInBounds(i - 1, j, matrix) and not visited[i - 1][j] and matrix[i - 1][j] == 1:
        unvisitedNeighbours.append([i - 1, j])

    # check the right
    if isInBounds(i + 1, j, matrix) and not visited[i + 1][j] and matrix[i + 1][j] == 1:
        unvisitedNeighbours.append([i + 1, j])

    # check the top
    if isInBounds(i, j - 1, matrix) and not visited[i][j - 1] and matrix[i][j - 1] == 1:
        unvisitedNeighbours.append([i, j - 1])

    # check the bottom
    if isInBounds(i, j + 1, matrix) and not visited[i][j + 1] and matrix[i][j + 1] == 1:
        unvisitedNeighbours.append([i, j + 1])

    return unvisitedNeighbours


def isInBounds(i, j, matrix):
    return not (i < 0 or j < 0 or i >= len(matrix[0]) or j >= len(matrix))


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

riverLengths(matrix)
