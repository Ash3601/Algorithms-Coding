def kmp(string, substring):
    if len(string) == 0 or len(substring) == 0:
        return False
    pattern = buildPattern(substring)
    return doesMatch(string, substring, pattern)


def buildPattern(substring):
    i = 1
    j = 0

    pattern = [-1] * len(substring)

    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            j += 1
            i += 1
        elif j > 0:
            j = pattern[j - 1] + 1

        else:  # if the potential match character is not found then we have to move forward
            i += 1

    return pattern


def doesMatch(string, substring, pattern):
    i = 0  # for string
    j = 0  # for substring

    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j-1] + 1
        else:
            i += 1
    return False


print(kmp('abcab', 'abc'))
