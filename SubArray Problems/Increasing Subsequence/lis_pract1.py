def getLongestIncreasingSubsequence(array):
    # Dynamic Programming
    lengths = [1] * len(array)
    sequences = [None] * len(array)
    maxLengthIdx = 0
    for idx in range(1, len(array)):
        currentNum = array[idx]
        for i in range(0, idx):
            previousNum = array[i]
            if currentNum > previousNum:
                lengths[idx] = max(lengths[idx], lengths[i] + 1)
                if lengths[i] + 1 >= lengths[idx]:
                    sequences[idx] = i
        if lengths[maxLengthIdx] < lengths[idx]:
            maxLengthIdx = idx
    print(sequences)
    return [lengths[maxLengthIdx], buildSequence(array, sequences, maxLengthIdx)]


def buildSequence(array, sequences, maxLengthIdx):
    sequence = []
    currentIdx = maxLengthIdx
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(getLongestIncreasingSubsequence(sequence))

# print(getLongestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
