class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)  # swapped in place Space: O(1)

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        # keep sifting up until we find the root
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def siftUp(self, startIdx, heap):
        parentIdx = (startIdx - 1) // 2  # gives the parent index
        while heap[parentIdx] > heap[startIdx] and startIdx > 0:
            self.swap(parentIdx, startIdx, heap)
            startIdx = parentIdx
            parentIdx = (startIdx - 1) // 2

    def siftDown(self, startIdx, endIdx, heap):
        childOneIdx = startIdx * 2 + 1
        while childOneIdx <= endIdx:  # to the leaf
            childTwoIdx = startIdx * 2 + 2 if startIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[startIdx] > heap[idxToSwap]:
                self.swap(startIdx, idxToSwap, heap)
                startIdx = idxToSwap
                childOneIdx = startIdx * 2 + 1
            else:
                break

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 1) // 2
        for parentIdx in reversed(range(firstParentIdx)):
            self.siftDown(parentIdx, len(array) - 1, array)
        return array

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


class Heap:
    def __init__(self, array, isMinHeap=True):
        self.isMinHeap = isMinHeap
        self.heap = self.buildHeap(array)  # swapped in place Space: O(1)

    def comparision(self, i, j, heap):
        if self.isMinHeap:
            return heap[i] > heap[j]
        return heap[i] < heap[j]

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        # keep sifting up until we find the root
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def siftUp(self, startIdx, heap):
        parentIdx = (startIdx - 1) // 2  # gives the parent index
        while self.comparision(parentIdx, startIdx, heap) and startIdx > 0:  # comparision
            self.swap(parentIdx, startIdx, heap)
            startIdx = parentIdx
            parentIdx = (startIdx - 1) // 2

    def siftDown(self, startIdx, endIdx, heap):
        childOneIdx = startIdx * 2 + 1
        while childOneIdx <= endIdx:  # to the leaf
            childTwoIdx = startIdx * 2 + 2 if startIdx * 2 + 2 <= endIdx else -1
            # comparision
            if childTwoIdx != -1 and self.comparision(childOneIdx, childTwoIdx, heap):
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if self.comparision(startIdx, idxToSwap, heap):
                self.swap(startIdx, idxToSwap, heap)
                startIdx = idxToSwap
                childOneIdx = startIdx * 2 + 1
            else:
                break

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 1) // 2
        for parentIdx in reversed(range(firstParentIdx)):
            self.siftDown(parentIdx, len(array) - 1, array)
        return array

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


heap = Heap([122, 34, 545, 12, 456, 66, 70, 71, 69], False)
print(heap.heap)
print(heap.peek(), 'Peek')
heap.insert(1000)
print(heap.peek(), 'Peek')

while len(heap.heap):
    print(heap.remove())
