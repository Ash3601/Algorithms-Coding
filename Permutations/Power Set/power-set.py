

def powerset(array):
    # create a subsets array to store them
    subsets = [[]]  # a power set always contains an empty set

    # for every number in array
    # we are gonna go through the subset of the subsets array and add it
    for num in array:
        for i in range(len(subsets)):
            currSubset = subsets[i][:]
            currSubset.append(num)
            subsets.append(currSubset[:])

    return subsets


s = powerset([1, 2, 3])
print(s)


def getPermutations(array):
	if len(array) == 0:
		return []

	result = []

    helper(array, 0, len(array),result)
	# print ('result', result)
	return result

def helper(a, left, right, result):
	if left == right:
		# print ('if', a)
		
		result.append(a[:])
		# print ('result array', result)
	else:
		for i in range(left, right):
			a[left], a[i] = a[i], a[left]
			# print ('1', a)
			helper(a, left + 1, right, result)
			a[left], a[i] = a[i], a[left]
			# print('2', a)
		
	
