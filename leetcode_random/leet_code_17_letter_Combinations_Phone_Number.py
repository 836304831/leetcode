# !/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2020/9/17 下午5:28
# @Author  : changqingai
# @FileName: leet_code_17_letter_Combinations_Phone_Number.py
# ----------------------------


class Solution(object):
    num_letter_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        ans = []
        for idx, digit in enumerate(digits):
            digit_letter_list = self.num_letter_map.get(digit)
            c_len = len(ans)
            if c_len == 0:
                ans = digit_letter_list
                continue
            tmp_list = []
            for i in range(0, c_len):
                for j in range(0, len(digit_letter_list)):
                    tmp_list.append(ans[i] + digit_letter_list[j])
            ans = tmp_list
        return ans


if __name__ == "__main__":
    ss = ["23", "235", ]
    for idx, s in enumerate(ss):
        result = Solution().letterCombinations(s)
        print(result)
        # assert s_ans[idx] == result
        # print("result: {}".format(result))
