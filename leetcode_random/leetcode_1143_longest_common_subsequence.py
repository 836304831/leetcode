class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 332 ms
        # 21.5 MB
        if text1 == "" or text2 == "":
            return 0
        dp = [[0 for _ in range(0, len(text2) + 1)] for _ in range(0, len(text1) + 1)]
        print(len(dp), len(dp[0]))
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[len(text1)][len(text2)]


if __name__ == "__main__":
    text1, text2 = "abcde", "ace"
    # text1, text2 = "abc", "abc"
    # text1, text2 = "abc", "def"
    result = Solution().longestCommonSubsequence(text1, text2)
    print("result: {}".format(result))
