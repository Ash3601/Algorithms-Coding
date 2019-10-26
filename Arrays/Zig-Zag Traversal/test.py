# class Solution:
#     def isInBounds(self, row, col, n):
#         print("In bounds for row col", row, col)
#         lastRow = lastCol = n - 1
#         return not (row > lastRow or col > lastCol or row < 0 or col < 0)

#     def printMatrix(self, matrix):
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 print(matrix[i][j], end=" ")
#             print()

#     def orangesRotting(self, grid):
#         row = 0
#         col = 0
#         n = len(grid[0])
#         minutes = 0
#         isUpdated = False
#         while row < n and col < n:
#             if grid[row][col] == 2:
#                 if self.isInBounds(row - 1, col, n) and grid[row - 1][col] == 1:
#                     # print("row - 1", row - 1, "col", col)
#                     grid[row - 1][col] = 2
#                     isUpdated = True
#                     # minutes += 1
#                 if self.isInBounds(row + 1, col, n) and grid[row + 1][col] == 1:
#                     # print("row + 1", row + 1, "col", col)
#                     grid[row + 1][col] = 2
#                     isUpdated = True
#                     # minutes += 1
#                 if self.isInBounds(row, col - 1, n) and grid[row][col - 1] == 1:
#                     # print("row", row - 1, "col - 1", col - 1)
#                     grid[row][col - 1] = 2
#                     isUpdated = True
#                     # minutes += 1
#                 if self.isInBounds(row, col + 1, n) and grid[row][col + 1] == 1:
#                     # print("row", row, "col + 1", col + 1)
#                     grid[row][col + 1] = 2
#                     isUpdated = True

#                     # minutes += 1
#                 if isUpdated:
#                     minutes += 1
#                     isUpdated = False
#             self.printMatrix(grid)
#             # print("minutes", minutes, "row", row, "col", col)

#             col = col + 1
#             if col >= n:
#                 row = row + 1
#                 col = 0
#         print(minutes if minutes > 0 else - 1)


# sol = Solution()
# sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])


class Solution:

    def isInBounds(self, row, col, lastRow, lastCol):
        # print("In bounds for row col", row, col)
        # lastRow = lastCol = n - 1
        return not (row > lastRow or col > lastCol or row < 0 or col < 0)

    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print()

    def orangesRotting(self, grid):
        print("Initial Matrix")
        self.printMatrix(grid)
        print()
        row = 0
        col = 0
        n = len(grid[0])
        minutes = 0
        isUpdated = False
        lastRow = len(grid) - 1
        lastCol = len(grid[0]) - 1
        while row <= lastRow and col <= lastCol:
            if grid[row][col] == 2:
                if self.isInBounds(row - 1, col, lastRow, lastCol) and grid[row - 1][col] == 1:
                    # print("row - 1", row - 1, "col", col)
                    grid[row - 1][col] = 2
                    isUpdated = True
                    # minutes += 1
                if self.isInBounds(row + 1, col, lastRow, lastCol) and grid[row + 1][col] == 1:
                    # print("row + 1", row + 1, "col", col)
                    grid[row + 1][col] = 2
                    isUpdated = True
                    # minutes += 1
                if self.isInBounds(row, col - 1, lastRow, lastCol) and grid[row][col - 1] == 1:
                    # print("row", row - 1, "col - 1", col - 1)
                    grid[row][col - 1] = 2
                    isUpdated = True
                    # minutes += 1
                if self.isInBounds(row, col + 1, lastRow, lastCol) and grid[row][col + 1] == 1:
                    # print("row", row, "col + 1", col + 1)
                    grid[row][col + 1] = 2
                    isUpdated = True

                    # minutes += 1
                if isUpdated:
                    minutes += 1
                    isUpdated = False
            # self.printMatrix(grid)
            # print("minutes", minutes, "row", row, "col", col)

            col = col + 1
            if col == n:
                row = row + 1
                col = 0
            self.printMatrix(grid)
            print()
        print("Minutes", minutes)
        if self.allRotten(grid):
            return minutes
        else:
            return -1

    def allRotten(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return False
        return True


sol = Solution()
sol.orangesRotting([[1, 1, 2, 0, 2, 0]])
