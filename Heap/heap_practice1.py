# Sift Up
# Sift Down
# Insert
# Build Heap Inplace
# Peak


class MinHeap:

    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # We start from the last parent node and keep performing sift down operations on it until we reach the root or index 0
        firstparentNodeIdx = (len(array) - 1 - 1) // 2

        for currentIdx in range(firstparentNodeIdx, -1, -1):
            self.siftDown(currentIdx, array)
        return array

    def siftUp(self, currentIdx, heap):

        parentIdx = (currentIdx - 1) // 2  # parent node idx

        # while it does not reach to the root node
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2  # parent node idx

    def siftDown(self, currentIdx, heap):
        endIdx = len(heap) - 1
        while currentIdx < endIdx:
            if currentIdx * 2 + 1 <= endIdx:
                childOneIdx = currentIdx * 2 + 1
            else:
                break
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else None

            if childTwoIdx is not None and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            # Now we need to check if we need to swap the parentNode
            if heap[currentIdx] > heap[idxToSwap]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
            else:
                break

    def insertValue(self, value):
        # append value at the last of the heap
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        # Swap the last value with the first and do sift down operation
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToBeRemoved = self.heap.pop()
        # To retain Heap Property
        self.siftDown(0, self.heap)
        return valueToBeRemoved

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


# AWESOME
# array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
# heap = MinHeap(array)
# while len(array) != 0:
#     print(heap.remove(), end=' ')
array = [1, 2, 3, 4, 5]
heap = MinHeap(array)
while len(array) != 0:
    print(heap.remove(), end=' ')
