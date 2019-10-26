def generate(numRows):
    res = [[1], [1, 1]]
    # TODO corner case for 1 and 2 rows
    for row in range(3, numRows + 1):
        curRes = []
        first = 0
        second = first + 1

        for i in range(row):

            if i == 0 or i == row - 1:
                curRes.append(1)
            else:
                if first < len(res[-1]) - 1:
                    curRes.append(res[-1][first] + res[-1][second])
                    first += 1
                    second = first + 1
        res.append(curRes)

    print(res)


generate(5)
