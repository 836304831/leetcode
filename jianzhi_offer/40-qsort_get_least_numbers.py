# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/16 10:57 上午
# @Author  : changqingai
# @FileName: 40_get_least_numbers.py
# ----------------------------


class Solution:
    def getLeastNumbers(self, arr, k):
        # 超出时间限制
        if k == 0:
            return []
        pivot = self._partition(arr, 0, len(arr) - 1)
        while pivot != k - 1:
            if pivot > k - 1:
                pivot = self._partition(arr, 0, pivot - 1)
            else:
                pivot = self._partition(arr, pivot + 1, len(arr) - 1)
        return arr[: k]

    def _partition(self, arr, left, right):
        key = arr[left]
        while left < right:
            while left < right and arr[right] >= key:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= key:
                left += 1
            arr[right] = arr[left]
        arr[left] = key
        return left


if __name__ == "__main__":
    # nums = [3, 2, 1]
    # k = 2
    # nums = [0, 1, 2, 1]
    # k = 1
    nums = [0, 0, 0, 2, 0, 5]
    k = 0
    result = Solution().getLeastNumbers(nums, k)
    print('result, ', result)
