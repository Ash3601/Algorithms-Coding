def getLCSLength(str1, str2):
    # Using dp
    # create a matrix to go over the cases
    # the base case is empty string
    # considering the empty string as the ans for it so 0
    lcs = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    # iterate over the lcs and keep appending to the length if both the chars matches
    for i in range(1, len(lcs)):
        for j in range(1, len(lcs[0])):
            # j cols iterations
            # since I considered the base case in creating the matrix thus I have to use 1 index less
            if str1[j - 1] == str2[i - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    # return the last value since at this point we have moved over all the values.
    return lcs[-1][-1]


length = getLCSLength("ABC", "AB")
print(length)
