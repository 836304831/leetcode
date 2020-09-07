# !/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2020/9/4 下午4:20
# @Author  : changqingai
# @FileName: im_3_longest_substring_without_repeating_characters.py
# ----------------------------


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_ch_map = {}
        ans = 0
        for idx, ch in enumerate(s):
            if longest_ch_map.__contains__(ch):
                self.update_ch_map(longest_ch_map, longest_ch_map.get(ch))
                longest_ch_map[ch] = idx
            else:
                longest_ch_map[ch] = idx
                if ans < len(longest_ch_map):
                    ans = len(longest_ch_map)
        return ans

    def update_ch_map(self, ch_set, pos):
        pop_ch_list = []
        for key, value in ch_set.items():
            if value <= pos:
                pop_ch_list.append(key)
        for ch in pop_ch_list:
            ch_set.pop(ch)


if __name__ == "__main__":

    ss = ["pwwkew", "abcabcbb", "", "bbbbb"]
    s_ans = [3, 3, 0, 1]
    for idx, s in enumerate(ss):
        result = Solution().lengthOfLongestSubstring(s)
        assert s_ans[idx] == result
        print("result: {}".format(result))
