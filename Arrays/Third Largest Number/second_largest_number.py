def second_largest(arr):
    max = float('-inf')
    max2 = float('-inf')

    for i in range(len(arr)):
        if max < arr[i]:
            max2 = max
            max = arr[i]
        elif arr[i] > max2 and max != arr[i]:
            max2 = arr[i]
    print(max, max2)


l = [2, 1, 3, 4, 5]
second_largest(l)
