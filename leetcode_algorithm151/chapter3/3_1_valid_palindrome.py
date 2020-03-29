class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 60 ms
        # 13 MB
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdecimal():
                left += 1
            while left < right and not s[right].isalpha() and not s[right].isdecimal():
                right -= 1
            if s[left].upper() == s[right].upper():
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    # s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # s = "0P"
    # s = "123aba321"
    s = "123aaba22"
    result = Solution().isPalindrome(s)
    print("result: {}".format(result))
