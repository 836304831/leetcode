# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/4/19 3:43 下午
# @Author  : changqingai
# @FileName: 6_7_sort_colors.py
# ----------------------------


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 36 ms	14.7 MB
        red_index = 0
        blue_index = len(nums) - 1
        i = 0
        while i <= blue_index:
            if nums[i] == 0:
                nums[i] = nums[red_index]
                nums[red_index] = 0
                red_index += 1
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[blue_index]
                nums[blue_index] = 2
                blue_index -= 1
            else:
                i += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    # 输出：[0, 0, 1, 1, 2, 2]

    # nums = [2, 0, 1]
    # # 输出：[0, 1, 2]
    #
    # nums = [0]
    # # 输出：[0]
    #
    # nums = [1]
    # 输出：[1]

    Solution().sortColors(nums)
    print("result: {}".format(nums))
