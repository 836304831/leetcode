# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 4:46 下午
# @Author  : changqingai
# @FileName: 48_length_of_longest_substring.py
# ----------------------------


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 	92 ms	15.3 MB
        if len(s) == 0:
            return 0

        dp = [0 for i in range(0, len(s))]
        ch_idx_map = {}

        max_len = 1
        for i in range(0, len(s)):
            if i == 0:
                ch_idx_map[s[i]] = 0
                dp[0] = 1
                continue
            ch_len = i - ch_idx_map.get(s[i], -1)
            if ch_len > dp[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = ch_len
            ch_idx_map[s[i]] = i
            if max_len < dp[i]:
                max_len = dp[i]
        return max_len


if __name__ == "__main__":
    # str_value = "abcabcbb"
    # str_value = "bbbbb"
    str_value = "pwwkew"
    ans = Solution().lengthOfLongestSubstring(str_value)
    print("ans: ", ans)
