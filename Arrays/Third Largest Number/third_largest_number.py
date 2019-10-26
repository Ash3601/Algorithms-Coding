def second_largest(arr):
    max = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    for i in range(len(arr)):
        if max <= arr[i]:
            max3 = max2
            max2 = max
            max = arr[i]
        elif arr[i] >= max2 and max != arr[i]:
            max2 = arr[i]
        elif arr[i] >= max3 and max != arr[i] and max2 != arr[i]:
            max3 = arr[i]
    print(max, max2, max3)


l = [2, 1, 3, 4, 5]
l = [4, 4, 4]
l = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
l = [10, 5, 9, 10, 12]
second_largest(l)
