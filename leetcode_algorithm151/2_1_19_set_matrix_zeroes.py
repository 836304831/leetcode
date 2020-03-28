class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 32 ms
        # 13.5 MB
        if len(matrix) == 0:
            return
        if len(matrix[0]) == 0:
            return
        row_zero, col_zero = False, False
        m, n = len(matrix), len(matrix[0])
        for i in range(0, m):
            if matrix[i][0] == 0:
                row_zero = True
                break
        for i in range(0, n):
            if matrix[0][i] == 0:
                col_zero = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_zero:
            for i in range(0, m):
                matrix[i][0] = 0
        if col_zero:
            for i in range(0, n):
                matrix[0][i] = 0


if __name__ == "__main__":
    matrix = [
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]
            ]
    result = Solution().setZeroes(matrix)
    print("result: {}".format(matrix))
