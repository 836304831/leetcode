class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 32 ms
        # 12.7 MB
        if n == 1:
            return 1
        if n == 2:
            return 2
        f1, f2 = 1, 2
        for i in range(2, n):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3


if __name__ == "__main__":
    n = 3
    result = Solution().climbStairs(n)
    print("result: {}".format(result))
