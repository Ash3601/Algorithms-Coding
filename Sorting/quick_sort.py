
def swap(leftIdx, rightIdx, array):
    array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]


def quickSortHelper(array, startIdx, endIdx):

    # pivot = partition(array, startIdx, endIdx)
    if startIdx >= endIdx:
        return

    pivotIdx = startIdx

    leftIdx = startIdx + 1
    rightIdx = endIdx

    while leftIdx <= rightIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(rightIdx, pivotIdx, array)

    # quickSortHelper(array, startIdx, rightIdx - 1)
    # quickSortHelper(array, rightIdx + 1, endIdx)
    # To make the Space Complexity in O(logN)
    # We will first let smaller subarrays to run in the
    # Call stack and then the bigger subarrays will follow itself
    # right idx is the index where the current pivot is
    leftSubarrayIsSmaller = rightIdx - 1 - \
        startIdx < endIdx - (rightIdx + 1)

    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


l = [3, 1, 2, 4, 5]
l = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
l = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7, 101, 3324, 2342356, 76745]

quickSortHelper(l, 0, len(l)-1)
print(l)
