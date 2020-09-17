# !/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2020/9/17 下午5:18
# @Author  : changqingai
# @FileName: leetcode_11_container_with_most_water.py
# ----------------------------


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                left += 1
            else:
                area = (right - left) * height[right]
                right -= 1
            if ans < area:
                ans = area
        return ans


if __name__ == "__main__":
    ss = [[1, 8, 6, 2, 5, 4, 8, 3, 7], ]
    s_ans = [49]
    for idx, s in enumerate(ss):
        result = Solution().maxArea(s)
        print(result)
        assert s_ans[idx] == result
        print("result: {}".format(result))
