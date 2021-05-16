# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/16 2:07 下午
# @Author  : changqingai
# @FileName: 03_find_repeat_number.py
# ----------------------------


class Solution:
    def findRepeatNumber(self, nums):
        # 60 ms	23.4 MB
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue

            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                tmp = nums[i]
                nums[i] = nums[nums[i]]
                nums[tmp] = tmp
            i += 1
        return -1


if __name__ == "__main__":
    nums = [2, 3, 1, 0, 2, 5, 3]
    result = Solution().findRepeatNumber(nums)
    print('result,', result)
