def kadanesAlgorithm(array):
    if len(array) == 1:
        return array
    maxEndingHere = array[0]
    maxSoFar = array[0]

    for index in range(1, len(array)):
        # ? Whole kadane algorithm is in the below formulas
        maxEndingHere = max(maxEndingHere + array[index], array[index])
        maxSoFar = max(maxEndingHere, maxSoFar)
    return maxSoFar
    # pass


def kadanesAlgorithm(array):
    currentIndex = 0
    if len(array) == 1:
        return array
    maxEndingHere = array[0]
    maxSoFar = array[0]

    for index in range(1, len(array)):
        # ? Whole kadane algorithm is in the below formulas
        maxEndingHere = max(maxEndingHere + array[index], array[index])
        if maxEndingHere == array[index]:
            currentIndex = index
        maxSoFar = max(maxEndingHere, maxSoFar)
    print(currentIndex)
    return maxSoFar
    # pass


input = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(input))


input = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(input))
