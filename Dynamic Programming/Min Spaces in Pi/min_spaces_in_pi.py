def findMinSpaces(pi, numbers):
    numberTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numberTable, {}, 0)
    print(minSpaces)


callStack = 1


def getMinSpaces(pi, numberTable, cache, idx):
    global callStack
    if idx == len(pi):
        return -1

    if idx in cache:
        return cache[idx]
    minSpaces = float('inf')
    for i in range(idx, len(pi)):
        prefix = pi[idx: i+1]
        if prefix in numberTable:
            print('In call stack', callStack)
            callStack += 1
            print('Value of minSpaces before call stacks', minSpaces)
            print('Cache ', cache)
            print('gS(', i + 1, ')')
            minSpaceInSuffix = getMinSpaces(pi, numberTable, cache, i + 1)
            print('Value of minSpaces after call stacks', minSpaces)
            minSpaces = min(minSpaces, minSpaceInSuffix + 1)
    cache[idx] = minSpaces
    print('Cache outside for loop ', cache)
    return cache[idx]


findMinSpaces('314159', ['3141', '5', '31', '2', '4159', '9', '42'])
