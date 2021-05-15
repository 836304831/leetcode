# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 5:38 下午
# @Author  : changqingai
# @FileName: 50_first_uniq_char.py
# ----------------------------


class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 	176 ms	15 MB
        if s == "":
            return " "
        ch_times_map = {}
        for i in range(0, len(s)):
            if ch_times_map.__contains__(s[i]):
                ch_times_map[s[i]] += 1
            else:
                ch_times_map[s[i]] = 1
        for i in range(0, len(s)):
            if ch_times_map[s[i]] == 1:
                return s[i]
        return " "


if __name__ == "__main__":
    s = "abaccdeff"
    s = ""
    ans = Solution().firstUniqChar(s)
    print("ans: ", ans)