# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 7:13 下午
# @Author  : changqingai
# @FileName: 51_reverse_pairs.py
# ----------------------------


class Solution:
    def __init__(self):
        self.ans = 0

    def reversePairs(self, nums) -> int:
        # 	7928 ms	20.6 MB
        if len(nums) == 0:
            return 0
        self.ans = 0
        self._merge_sort(nums)
        return self.ans

    def _merge(self, nums1, nums2):
        result = []
        first_idx = len(nums1) - 1
        second_idx = len(nums2) - 1
        while first_idx >= 0 and second_idx >= 0:
            if nums1[first_idx] > nums2[second_idx]:
                self.ans += second_idx + 1
                result.insert(0, nums1[first_idx])
                first_idx -= 1
            else:
                result.insert(0, nums2[second_idx])
                second_idx -= 1
        while first_idx >= 0:
            result.insert(0, nums1[first_idx])
            first_idx -= 1
        while second_idx >= 0:
            result.insert(0, nums2[second_idx])
            second_idx -= 1
        return result

    def _merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        split_len = len(nums) // 2
        nums1 = self._merge_sort(nums[0: split_len])
        nums2 = self._merge_sort(nums[split_len:])
        nums = self._merge(nums1, nums2)
        return nums


if __name__ == "__main__":
    # nums = [7, 5, 6, 4]  # 5
    nums = [5, 4, 3, 2, 1]   # 10
    ans = Solution().reversePairs(nums)
    print("ans: ", ans)
