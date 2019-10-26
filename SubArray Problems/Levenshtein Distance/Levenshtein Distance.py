def levenshteinDistance(str1, str2):
    # We gonna use dynamic programming 
    # DP
    # Create a edits
    # The base case will be the empty string 
    edits = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    # Init the edits
    for i in range(len(edits[0])):
        edits[0][i] = i
    
    # Init the first column
    for i in range(len(edits)):
        edits[i][0] = i

    # We start looping through the string with i - 1 indices 
    # and if we find both the value as same then we use the diagonal value
    # otherwise we find the min value of the three and add one for the operation
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                edits[i][j] = edits[i-1][j-1]
            # otherwise we do the min value operation 
            else:
                edits[i][j] = min(edits[i-1][j], edits[i][j-1], edits[i-1][j-1]) + 1

    print ("Min value for the Levenshtein Distance", edits[-1][-1])                           



levenshteinDistance("abc", "yabd")    
