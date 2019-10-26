def permutations(array):
    permutations = []
    permute(array, 0, permutations)
    return permutations


def permute(array, i, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permute(array, i+1, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


perms = permutations([1, 2, 3])
print(perms)
