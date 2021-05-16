# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/16 11:37 上午
# @Author  : changqingai
# @FileName: 40-2heap_get_least_numbers.py
# ----------------------------


class Solution:
    def getLeastNumbers(self, arr, k):
        # 	124 ms	15.9 MB
        if len(arr) <= k:
            return arr
        if k == 0:
            return []
        nums_k = [arr[i] for i in range(0, k)]
        nums_k = self._build_heap(nums_k)
        for i in range(k, len(arr)):
            if arr[i] > nums_k[0]:
                continue
            nums_k[0] = arr[i]
            self._heap_adjust(nums_k, 0)
        return nums_k

    def _build_heap(self, nums_k):
        i = len(nums_k) // 2 - 1
        while i >= 0:
            self._heap_adjust(nums_k, i)
            i -= 1
        return nums_k

    def _heap_adjust(self, nums, i):
        # 下标要特别注意
        left_child = i * 2 + 1
        right_child = i * 2 + 2
        while left_child < len(nums) or right_child < len(nums):
            wrap_child = left_child
            if right_child < len(nums) and nums[left_child] < nums[right_child]:
                wrap_child = right_child
            if nums[i] < nums[wrap_child]:
                tmp = nums[wrap_child]
                nums[wrap_child] = nums[i]
                nums[i] = tmp
                i = wrap_child
                left_child, right_child = i * 2 + 1, i * 2 + 2
            else:
                break


if __name__ == "__main__":
    # nums = [3, 2, 1]
    # k = 2
    # nums = [0, 1, 2, 1]
    # k = 1
    # nums = [0, 0, 0, 2, 0, 5]
    # k = 0
    # nums = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    # k = 8
    nums = [3, 2, 1, 4, -1, 2, 8]
    k = 5
    result = Solution().getLeastNumbers(nums, k)
    print('result, ', result)
