class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 32 ms
        # 12.9 MB
        s = s.strip()
        if len(s) == 0:
            return False

        p = 0
        is_valid, p = self.is_int(s, p)
        if p == len(s):
            return is_valid

        if s[p] == ".":
            p += 1
            is_valid_tmp, p = self.is_unsigned_int(s, p)
            is_valid = is_valid or is_valid_tmp

        if p == len(s):
            return is_valid

        if s[p] == "e" or s[p] == "E":
            p += 1
            is_valid_tmp, p = self.is_int(s, p)
            is_valid = is_valid and is_valid_tmp
        return is_valid and p == len(s)

    def is_int(self, s, p):
        if p < len(s) and (s[p] == "+" or s[p] == "-"):
            p += 1
        return self.is_unsigned_int(s, p)

    def is_unsigned_int(self, s, p):
        raw_p = p
        while p < len(s):
            if '0' <= s[p] <= '9':
                p += 1
            else:
                break
        return True if raw_p != p else False, p


if __name__ == "__main__":
    # s = "0"
    # s = " 0.1 "
    # s = "abc"
    # s = "1 a"
    # s = "2e10"
    # s = " -90e3   "
    # s = " 1e"
    # s = "e3"
    # s = " 6e-1"
    # s = " 99e2.5 "
    # s = "53.5e93"
    # s = " --6 "
    # s = "-+3"
    # s = "95a54e53"
    # s = ".1"
    # s = "."
    # s = ".0"
    # s = "3."
    # s = "0e"
    # s = "1 4"
    s = "2e0"
    result = Solution().isNumber(s)
    print("result: {}".format(result))