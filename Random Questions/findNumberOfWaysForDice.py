#! https://www.geeksforgeeks.org/dice-throw-dp-30/
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation:
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.


def numberWays(face, dices, target):
    table = [[0] * (target + 1) for dice in range(dices + 1)]
    for i in range(1, min(face + 1, target + 1)):
        table[1][i] = 1

    for dice in range(2, dices + 1):
        for targetValue in range(1, target + 1):
            for faceValue in range(1, min(face + 1, targetValue + 1)):
                table[dice][targetValue] += table[dice -
                                                  1][targetValue - faceValue]
            print(table)
    print(table)


numberWays(6, 2, 7)
