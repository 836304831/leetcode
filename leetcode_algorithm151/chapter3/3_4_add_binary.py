class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 28 ms
        # 13 MB
        ans = ""
        i, j = len(a) - 1 , len(b) - 1
        c = "0"
        while i >= 0 and j >= 0:
            if a[i] == "1" and b[j] == "1" and c == "0":
                ans = "0" + ans
                c = "1"
            elif a[i] == "1" and b[j] == "1" and c == "1":
                ans = "1" + ans
                c = "1"
            elif (a[i] == "1" or b[j] == "1") and c == "0":
                ans = "1" + ans
                c = "0"
            elif (a[i] == "1" or b[j] == "1") and c == "1":
                ans = "0" + ans
                c = "1"
            elif c == "0":
                ans = "0" + ans
                c = "0"
            else:
                ans = "1" + ans
                c = "0"
            i -= 1
            j -= 1
        while i >= 0:
            if a[i] == "1" and c == "1":
                ans = "0" + ans
                c = "1"
            elif (a[i] == "0" and c == "1") or (a[i] == "1" and c == "0"):
                ans = "1" + ans
                c = "0"
            else:
                ans = "0" + ans
                c = "0"
            i -= 1
        while j >= 0:
            if b[j] == "1" and c == "1":
                ans = "0" + ans
                c = "1"
            elif (b[j] == "0" and c == "1") or (b[j] == "1" and c == "0"):
                ans = "1" + ans
                c = "0"
            else:
                ans = "0" + ans
                c = "0"
            j -= 1
        if c == "1":
            ans = "1" + ans
        return ans


if __name__ == "__main__":
    a, b = "11", "1"
    # a, b = "1010", "1011"
    result = Solution().addBinary(a, b)
    print("result: {}".format(result))
