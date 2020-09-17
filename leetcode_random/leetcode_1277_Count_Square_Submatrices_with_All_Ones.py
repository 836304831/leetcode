# !/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2020/9/17 下午7:02
# @Author  : changqingai
# @FileName: leetcode_1277_Count_Square_Submatrices_with_All_Ones.py
# ----------------------------


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        """	800 ms	30 MB """
        # 记录当前的正方行的左上方起始点和长度，一次在已得到的正方形上进行判断长度大于1的正方形
        base_squares_map = {}
        squares_map = {}

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 1:
                    squares_map[(i, j)] = 1
                    base_squares_map[(i, j)] = 1
        ans = len(squares_map)

        while len(squares_map) > 0:
            c_quares_map = {}
            for key, length in squares_map.items():
                i, j = key
                row = i + length
                col = j + length
                is_square = True
                for k in range(0, length + 1):

                    if (row, j + k) in base_squares_map:
                        continue
                    is_square = False
                    break
                if not is_square:
                    continue
                for k in range(0, length + 1):
                    if (i + k, col) in base_squares_map:
                        continue
                    is_square = False
                    break
                if is_square:
                    c_quares_map[(i, j)] = length + 1
            squares_map = c_quares_map
            ans += len(squares_map)
        return ans


if __name__ == "__main__":
    # matrix =\
    #     [[0, 1, 1, 1],
    #     [1, 1, 1, 1],
    #     [0, 1, 1, 1]]

    # matrix = [
    #     [1, 0, 1],
    #     [1, 1, 0],
    #     [1, 1, 0]
    # ]
    # matrix = [[0,0,0],[0,1,0],[0,1,0],[1,1,1],[1,1,0]]   # 8
    matrix = [[1,1,0,0,1],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,0,1],[0,0,1,0,1]]  # 19
    result = Solution().countSquares(matrix)
    print(result)
