# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/13 10:35 上午
# @Author  : changqingai
# @FileName: 42_max_sub_array_sum.py
# ----------------------------


class Solution:
    def maxSubArray(self, nums):
        # 60 ms	18.4 MB
        max_here = max_value = nums[0]
        for i in range(1, len(nums)):
            if max_here <= 0:
                max_here = nums[i]
            else:
                max_here += nums[i]
            if max_value < max_here:
                max_value = max_here
        return max_value


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = Solution().maxSubArray(nums)
    print('result: {}'.format(result))
