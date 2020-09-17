# !/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2020/9/4 下午4:57
# @Author  : changqingai
# @FileName: leetcode_6_zigzag_conversion.py
# ----------------------------


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
            192 ms	21.5 MB	Python3
        """
        if numRows == 1:
            return s
        max_col = len(s) // (2 * numRows - 2)
        period_len = 2 * numRows - 2
        period_col = numRows - 1
        ans = [""] * period_col * (max_col + 1) * numRows
        for i in range(0, len(s)):

            # 第几个周期
            period = i // period_len
            # 第几行
            mod = i % period_len

            # 上行
            if mod >= numRows:
                row = numRows - (mod - numRows) - 2
            # 下行
            else:
                row = mod

            col = period * period_col if mod < numRows else period * period_col + (mod - numRows + 1)
            index = (period_col * (max_col + 1)) * row + col
            ans[index] = s[i]

        return "".join(ans)


if __name__ == "__main__":
    ss = [["PAYPALISHIRING", 3], ["PAYPALISHIRING", 4], ["", 1]]
    s_ans = ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", ""]
    for idx, s in enumerate(ss):
        result = Solution().convert(s[0], s[1])
        print(result)
        assert s_ans[idx] == result
        print("result: {}".format(result))
