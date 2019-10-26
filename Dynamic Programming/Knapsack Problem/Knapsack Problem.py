def knapsackProblem(items, capacity):
    # we are gonna be using dp
    # the base case will gonna be no item with 0 weight
    matrix = [[0 for i in range(0, (capacity) + 1)]
              for j in range(len(items) + 1)]

    # Now we begin to iterate through the items
    for i in range(1, len(items) + 1):
        # since we took the base case into account
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        # For each of the capacities until the given capacity
        for capacity in range(1, capacity + 1):
            # if it fits in the bag then we take the item

            if currentWeight <= capacity:
                # either we take the item or we remove it we get the max out of two
                matrix[i][capacity] = max(
                    matrix[i-1][capacity], matrix[i-1][capacity - currentWeight] + currentValue)
            else:
                matrix[i][capacity] = matrix[i-1][capacity]

    print(matrix[-1][-1], getSequences(matrix, items))


def getSequences(matrix, items):
    sequences = []
    idx = len(matrix) - 1
    capacity = len(matrix[0]) - 1
    while idx > 0:
        # we check if the value at above item matches the value
        # and if it does then its hinting us that that value is not used

        if matrix[idx][capacity] == matrix[idx - 1][capacity]:
            idx -= 1
        else:
            # if the values are differenet that signifies that the current item is added in the bag
            # hence we need to add it to the sequences
            sequences.append(idx - 1)
            capacity = capacity - items[idx - 1][1]
            idx -= 1
        if capacity == 0:
            break
    return sequences


knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10)
