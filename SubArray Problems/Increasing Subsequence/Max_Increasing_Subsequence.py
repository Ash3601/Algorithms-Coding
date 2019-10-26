def mis(arr):
    # create
    sums = arr[:]
    # sequence array
    sequences = [None] * len(arr)
    maxSumIdx = 0
    for i in range(len(arr)):
        currentNum = arr[i]
        for j in range(0, i):
            otherNum = arr[j]

            if otherNum < currentNum and sums[j] + currentNum > sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    print(sums[maxSumIdx], buildSequence(arr, sequences, maxSumIdx))


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


arr = [8, 12, 2, 3, 15, 5, 7]
mis(arr)
