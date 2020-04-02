class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 752 ms
        # 12.9 MB
        if len(s) == 0:
            return s
        ans = s[0]
        for i in range(0, len(s)):
            l, k = i - 1, i + 1
            while l >= 0 and k < len(s):
                if s[l] == s[k]:
                    l -= 1
                    k += 1
                    continue
                break
            if len(ans) < (k - l):
                ans = s[l+1: k]
            l, k = i - 1, i
            while l >= 0 and k < len(s):
                if s[l] == s[k]:
                    l -= 1
                    k += 1
                    continue
                break
            if len(ans) < (k - l):
                ans = s[l + 1: k]
        return ans

    def longestPalindromeDp(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 2980 ms
        # 21.3 MB
        if len(s) == 0:
            return s
        max_len = 1
        max_i = 0
        max_j = 0
        dp = [[False for j in range(False, len(s))] for i in range(0, len(s))]
        for i in range(0, len(s)):
            dp[i][i] = True
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_len = 2
                max_i = i
                max_j = i + 1

        for j in range(1, len(s)):
            for i in range(0, j):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_i = i
                        max_j = j
                        max_len = j - i + 1
        return s[max_i:max_j + 1]


if __name__ == "__main__":
    # str = "babad"
    # str = "abacdfgdcaba"
    # str = "cbbd"
    str = "aaaa"
    # result = Solution().longestPalindrome(str)
    result = Solution().longestPalindromeDp(str)
    print("result: {}".format(result))
