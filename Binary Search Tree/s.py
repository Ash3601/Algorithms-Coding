def subArraySum2(arr, S):
    print(arr)
    # using the sliding window approach
    # lets create a var to slide over
    currS = arr[0]  # better to think it starts with the first element
    start = 0  # also create a start index
    # now we need to start sliding over the elements
    # until we found the sum or the array traversal does not finish
    for i in range(1, len(arr)+1):
        # while i <= len(arr):
          # start from 0th index until the end
        # print('Current item ', arr[i])

        # check if the current sum is greater than given Sum
        # if currS > S:
        # if it is the case then we need to remove the elements from the start
        # until it is equal to or smaller than the given sum
        while currS > S and start < i - 1:
            print('Current subtracted ', currS)
            currS -= arr[start]
            print('Current subtracted, current val ', currS)

            start += 1

        if currS == S:  # now if it is equal to the given sum
            # print('Start index ', start, 'End index ', i-1)
            print(start, i)
            return
        # else we need to add the element
        if i < len(arr):
            currS += arr[i]
        print('Sum added up', currS)
    # print('Not found')
    print(-1)


l = [15, 2, 4, 8, 9, 5, 10, 23]
# subArraySum(l, len(l), 12)
subArraySum2(l, 15)
