# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 2:45 下午
# @Author  : changqingai
# @FileName: 45_min_number.py
# ----------------------------

import functools

class Solution:

    def cmp(self, item1, item2):
        num1 = str(item1) + str(item2)
        num2 = str(item2) + str(item1)
        for i in range(0, len(num1)):
            if num1[i] < num2[i]:
                return -1
            elif num1[i] > num2[i]:
                return 1
        return 0

    def minNumber(self, nums):
        # 52 ms	14.7 MB
        nums.sort(key=functools.cmp_to_key(self.cmp))
        return "".join(list(map(str, nums)))


if __name__ == "__main__":
    # nums = [3, 30, 31, 345]
    # nums = [10, 2]
    nums = [3, 30, 34, 5, 9]
    ans = Solution().minNumber(nums)
    print("ans: ", ans)
