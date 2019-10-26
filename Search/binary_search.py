
def binarySearchHelper(array, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    print(low, high, mid)
    # if mid < 0 or mid > len(array) - 1:
    # return -1
    # if low == high and array[mid] != key:
    # return -1
    # Terminating condition
    # if the mid element of the array is equal to the ele to be searched
    print(array)
    if key == array[mid]:
        print("Value Found at %s" % (mid))
        return True

    elif key < array[mid]:
        return binarySearchHelper(array, low, mid - 1, key)
    else:
        return binarySearchHelper(array, mid + 1, high, key)


def binarySearch(array, key):
    array = sorted(array)
    print(array)
    binarySearchHelper(array, 0, len(array) - 1, key)


key = 100
array = [12, 14, 124, 10, 43, 51, 1]
binarySearch(array, key)
