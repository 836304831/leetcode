class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 788 ms
        # 21.6 MB
        p = self.remove_duplicate_stars(p)

        dp = [[False for _ in range(0, len(p) + 1)] for _ in range(0, len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            dp[0][i] = dp[0][i-1] and p[i-1] == "*"

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[len(s)][len(p)]

    def remove_duplicate_stars(self, p):
        if len(p) == 0:
            return p
        new_p = [p[0]]
        new_i = 0
        for i in range(1, len(p)):
            if p[i] == "*" and p[i] == new_p[new_i]:
                continue
            else:
                new_p.append(p[i])
                new_i += 1
        return "".join(new_p)

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 超时
        self.dp = {}
        p = self.remove_duplicate_stars(p)
        return self.loop_match(s, p)


    def loop_match(self, s, p):
        if (s, p) in self.dp:
            return self.dp[(s, p)]

        if s == p or p == "*":
            self.dp[(s, p)] = True
        elif s == "" or p == "":
            self.dp[(s, p)] = False
        elif p[0] == "?" or s[0] == p[0]:
            self.dp[(s, p)] = self.loop_match(s[1:], p[1:])
        elif p[0] == "*":
            self.dp[(s, p)] = self.loop_match(s[1:], p) or self.loop_match(s, p[1:])
        else:
            self.dp[(s, p)] = False
        return self.dp[(s, p)]


if __name__ == "__main__":
    # s, p = "aa", "a"
    # s, p = "aa", "*"
    # s, p = "cb", "?a"
    # s, p = "adceb", "*a*b"
    # s, p = "acdcb", "a*c?b"
    # s, p = "", "*"
    s, p = "aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab", "*ab***ba**b*b*aaab*b"
    result = Solution().isMatch(s, p)
    print("result: {}".format(result))
