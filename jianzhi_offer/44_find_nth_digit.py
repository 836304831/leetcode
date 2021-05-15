# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 11:48 上午
# @Author  : changqingai
# @FileName: 44_num_sequence_one_num.py
# ----------------------------


class Solution:
    def findNthDigit(self, n):
        # 	40 ms	14.7 MB
        digit = 1
        while True:
            count = self.count_of_int(digit)
            if n < count * digit:
                return self.find_num(n, digit)
            n -= count * digit
            digit += 1

    def begin_num(self, digit):
        if digit == 1:
            return 0
        return pow(10, digit - 1)

    def find_num(self, n, digit):
        num = self.begin_num(digit) + n // digit
        num_index = digit - n % digit

        for i in range(1, num_index):
            num = num // 10
        return num % 10

    def count_of_int(self, digit):
        if digit == 1:
            return 10
        return 9 * pow(10, digit - 1)


if __name__ == "__main__":
    n = 1001
    ans = Solution().findNthDigit(n)
    print("ans: ", ans)
