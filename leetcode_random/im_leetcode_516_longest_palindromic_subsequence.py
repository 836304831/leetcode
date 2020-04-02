class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1440 ms
        # 28.1 MB
        dp = [[0 for i in range(0, len(s))] for i in range(0, len(s))]

        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]


if __name__ == "__main__":
    # str = "bbbab"
    str = "cbbd"
    result = Solution().longestPalindromeSubseq(str)
    print("result: {}".format(result))
