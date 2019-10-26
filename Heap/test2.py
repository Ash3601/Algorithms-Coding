# HEAP THEORY AND NOTATIONS
# heap should satisfy some conditions
# Its a binary tree that satisfies two additional properties
# 1. A binary tree must have all of its levels filled up completely
# 2. except the last level, which if partially filled up should be filled from left to right.
# Eg.
#       8
#     /  \
#    12   23   (Valid Heap)
#   /  \
# 17    31
# For Min-Heap the value can be smaller than or equal to its children
# Heaps can be represented in the form of arrays or lists
# root -> i
# first children -> i*2 + 1
# second children -> i*2 + 2
# root -> floor((i-1) // 2)
# Sift Up -> Method continously pushes a newly inserted node to its correct position
# Removal: remove the root node
# In removal the root node is replaced with the last element in the heap array
# And we perform Sift Down operation to heapify
# Sift Down: We find the smallest(maximum value if its Max Heap) of the two and replace it with the root node.
# Sift Up/Down: O(logn)
# Time Complexity Build Heap: O(N) Since we called Sift Down on N nodes
# Space Complexity: O(1) Since we do not use extra space


# Inorder to build the heap
# We have to start from the last parent node apply Sift Down method.
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
    # Time: O(N)
    # Space: O(1)

    def buildHeap(self, array):
        firstParentNodeIdx = (len(array) - 2) // 2

        for currentIdx in reversed(range(firstParentNodeIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)

        return array  # in place swap

    # O(logN) time | O(1) space
	# Both the methods are same and either can be used
    def siftDown(self, currentIdx, endIdx, heap):
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
	
	def _siftDown(self, currentIdx, endIdx, heap):
		endIdx = len(heap) - 1
        childOneIdx = currentIdx * 2 + 1

        while childOneIdx <= endIdx:  # meaning that the child node is not present at the leaf node
            # If child one is present then we can calculate idx for child 2
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else None
            if childTwoIdx is not None and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            # now we got which of the childs (if both are present is smaller)
            if heap[currentIdx] > heap[idxToSwap]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                # recalculate the childs for while loop
                childOneIdx = currentIdx * 2 + 1
            else:
                # we are done heap condition satisfies
                break

    # O(logN) time | O(1) space
    def siftUp(self, currentIdx, heap):
        # we want the parent node of the node which is present at the currentIdx
        parentNodeIdx = (currentIdx - 1) // 2  # floor it down

        # strictly less than the parent node
        while currentIdx > 0 and heap[currentIdx] < heap[parentNodeIdx]:
            self.swap(currentIdx, parentNodeIdx, heap)
            # now the current node is present at the parentNodeIdx
            currentIdx = parentNodeIdx
            parentNodeIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):  # in heap we are only intrested in removing the root node
        # swap the root node with the last value
        self.swap(0, len(self.heap) - 1, self.heap)

        # then we remove the value
        valueToRemove = self.heap.pop()

        # We then sift down
        self.siftDown(0, len(self.heap) - 1, self.heap)

        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
