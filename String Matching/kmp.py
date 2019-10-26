def kmp(string, substring):
    pattern = buildPattern(substring)

    return doesMatch(string, substring, pattern)


def doesMatch(string, substring, pattern):
    i = 0
    j = 0

    # j is the index for the substring
    # j shows here how far we have reached
    # i is the index of the current string
    # stopping condition if len(substring) - j + i <= len(string) shows that there is still a string
    # that can be matched
    #! REMEMBER
    while i + len(substring) - j <= len(string):
        if substring[j] == string[i]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
    #! NOTE: We do not touch i in the whole process only j moves back and forth
        elif j > 0:  # meaning that the string did not matched but previously there were a match
            # j - 1 meaning the previous match
            j = pattern[j - 1] + 1

        # if j is 0 meaning there is no previous match
        else:
            i += 1
    # if we never hit the while loop then we return that the string was not found
    return False


def buildPattern(substring):
    # we start with two indices i and j
    i = 1
    j = 0

    # then we create a pattern array to store the position of the patterns matched
    pattern = [-1] * len(substring)

    # if both the characters at i and j are equal then we increment both i and j
    if substring[i] == substring[j]:
        pattern[i] = j
        i += 1
        j += 1
    # if j is greater than 0 then we may find the potential match of the character
    # at the index of the ith pattern + 1
    elif j > 0:
        # means we have a pattern to match
        # replace our j pointer
        # look at the previous position of the i and then move 1 ahead since that might be a potential character match
        j = pattern[i - 1] + 1
    else:  # if j is 0 then there is nothing to be matched before it thus we increment i
        # Note the only way that j can get zero is by using the second elif block
        # since all the elements have -1 as the value that means that
        # we come to j == 0 after j = -1 + 1 = 0
        i += 1
    return pattern


print(kmp('abcab', 'ab'))
