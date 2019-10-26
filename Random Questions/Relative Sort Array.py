def relativeSort(arr1, arr2):
    arr2Map = {}
    for number in arr1:
        if number not in arr2Map:
            arr2Map[number] = [number]
        else:
            arr2Map[number].append(number)
    print(arr2Map)
    relativesortedList = []
    for number in arr2:
        relativesortedList = relativesortedList + arr2Map[number]
        del arr2Map[number]
    print(arr2Map)
    secondList = []
    for numberList in arr2Map.values():
        for number in numberList:
            secondList.append(number)
    secondList.sort()
    print(secondList)
    print(relativesortedList + secondList)


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
relativeSort(arr1, arr2)
