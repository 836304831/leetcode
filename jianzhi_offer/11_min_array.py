# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/16 3:25 下午
# @Author  : changqingai
# @FileName: 11_min_array.py
# ----------------------------


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        # 	44 ms	15.3 MB
        left, right = 0, len(numbers) - 1
        mid = left
        while numbers[left] >= numbers[right]:
            mid = (left + right) // 2
            if right - left == 1:
                mid = right
                break
            if numbers[left] == numbers[mid] and numbers[mid] == numbers[right]:
                return self._order_find(numbers, left, right)
            if numbers[left] <= numbers[mid]:
                left = mid
            else:
                right = mid
        return numbers[mid]

    def _order_find(self, numbers, left, right):
        min_value = numbers[left]
        for i in range(left + 1, right + 1):
            if numbers[i] < min_value:
                min_value = numbers[i]
        return min_value


if __name__ == "__main__":
    # nums = [3, 4, 5, 1, 2]
    # nums = [2, 2, 2, 0, 1]
    # nums = [1, 3, 5]
    # nums = [1, 0, 1, 1, 1]
    nums = [1, 1, 1, 0, 1]
    result = Solution().minArray(nums)
    print('result,', result)
