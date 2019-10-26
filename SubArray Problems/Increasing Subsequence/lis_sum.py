def getMaxIncreasingSubsequence(array):
    # Dynamic Programming
    lengths = array[:]
    sequences = [None] * len(array)
    maxLengthIdx = 0
    for idx in range(1, len(array)):
        currentNum = array[idx]
        for i in range(0, idx):
            previousNum = array[i]
            if currentNum > previousNum:
                lengths[idx] = max(lengths[idx], lengths[i] + currentNum)
                sequences[idx] = i
        if lengths[maxLengthIdx] < lengths[idx]:
            maxLengthIdx = idx
    print(lengths)
    return [lengths[maxLengthIdx], buildSequence(array, sequences, maxLengthIdx)]


def buildSequence(array, sequences, maxLengthIdx):
    sequence = []
    currentIdx = maxLengthIdx
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


print(getMaxIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7]))
