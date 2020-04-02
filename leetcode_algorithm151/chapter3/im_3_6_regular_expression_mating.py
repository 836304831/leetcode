class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 60 ms
        # 13 MB
        if s is None and p is None:
            return False
        dp = [[False for j in range(0, len(p) + 1)] for i in range(0, len(s) + 1)]
        dp[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                if j + 1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]


if __name__ == "__main__":
    # s, p = "aab", "c*a*b"

    # s, p = "aa", "a*"
    # s, p = "mississippi", "mis*is*p*."
    # s, p = "ab", "abc **"
    s, p = "", ".*"
    result = Solution().isMatch(s, p)
    print("result: {}".format(result))
