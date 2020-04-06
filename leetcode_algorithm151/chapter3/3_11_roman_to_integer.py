class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 64 ms
        # 12.9 MB
        special_map = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4,
                       }
        normal_map = {"M": 1000, "D": 500, "C": 100,
                        "L": 50, "X": 10, "V": 5, "I": 1}

        if len(s) == 0:
            return 0
        i = 0
        ans = 0
        while i < len(s):
            if i + 1 < len(s) and special_map.__contains__(s[i:i+2]):
                ans += special_map[s[i:i+2]]
                i += 2
            else:
                ans += normal_map[s[i]]
                i += 1
        return ans


if __name__ == "__main__":

    # s = "III"
    # s = "IV"
    # s = "IX"
    # s = "LVIII"
    s = "MCMXCIV"
    result = Solution().romanToInt(s)
    print("result: {}".format(result))
