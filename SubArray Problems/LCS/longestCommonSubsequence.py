# this will be a more optimised version
# Space: O(M *N)
# Time: O(M * N)

# We will create additional values in the lcs matrix to keep track of the idx and the
#  sequences we are adding as well as its length


def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None]
            for x in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    for i in range(1, len(lcs)):
        for j in range(1, len(lcs[0])):
            if str1[j - 1] == str2[i - 1]:
                lcs[i][j] = [str1[j - 1], lcs[i - 1]
                             [j - 1][1] + 1, i - 1, j - 1]
            else:
                # lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1],
                                # key=lambda x: (x[1]))
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]

    printMatrix(lcs)
    print(buildSequence(lcs))


def buildSequence(lcs):
    i = len(lcs) - 1
    j = len(lcs[0]) - 1

    sequence = []

    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            sequence.append(lcs[i][j][0])
        i = lcs[i][j][2]
        j = lcs[i][j][3]

    return list(reversed(sequence))


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


longestCommonSubsequence("ABC", "AB")
