# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/16 3:03 下午
# @Author  : changqingai
# @FileName: 04_find_number_in_2darray.py
# ----------------------------


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        # 36 ms	18.7 MB
        if len(matrix) == 0:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == "__main__":
    nums = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 20
    result = Solution().findNumberIn2DArray(nums, target)
    print('result,', result)