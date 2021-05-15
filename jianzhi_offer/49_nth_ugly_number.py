# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 5:23 下午
# @Author  : changqingai
# @FileName: 49_nth_ugly_number.py
# ----------------------------


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 188 ms	15 MB
        ugly_nums = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        while len(ugly_nums) < n:
            num = min([ugly_nums[p2]*2, ugly_nums[p3] * 3, ugly_nums[p5] * 5])
            ugly_nums.append(num)
            while ugly_nums[p2] * 2 <= num:
                p2 += 1
            while ugly_nums[p3] * 3 <= num:
                p3 += 1
            while ugly_nums[p5] * 5 <= num:
                p5 += 1
        return ugly_nums[n - 1]


if __name__ == "__main__":
    n = 10
    ans = Solution().nthUglyNumber(n)
    print("ans: ", ans)