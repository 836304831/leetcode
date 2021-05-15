# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 4:36 下午
# @Author  : changqingai
# @FileName: 47_max_value.py
# ----------------------------


class Solution:
    def maxValue(self, grid):
        # 	88 ms	16.3 MB
        matrxi_value = [[0 for j in range(0, len(grid[i]))] for i in range(0, len(grid))]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                left = matrxi_value[i][j-1] if j - 1 >= 0 else 0
                up = matrxi_value[i-1][j] if i - 1 >= 0 else 0
                matrxi_value[i][j] = max(left, up) + grid[i][j]
        return matrxi_value[len(grid) - 1][len(grid[0]) - 1]


if __name__ == "__main__":
    # nums = [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1]
    # ]
    nums = [
        [1, 10, 3, 8],
        [12, 2, 9, 6],
        [5, 7, 4, 11],
        [3, 7, 16, 5]
    ]
    ans = Solution().maxValue(nums)
    print("ans: ", ans)
