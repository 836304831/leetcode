class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 16 ms
        # 12.8 MB
        if s == "":
            return 0
        s = s.strip()
        if s == "":
            return 0
        str_s = s.split(" ")
        return len(str_s[len(str_s) - 1])


if __name__ == "__main__":
    path = "Hello World "
    result = Solution().lengthOfLastWord(path)
    print("result:{}".format(result))
