class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 24 ms
        # 12.8 MB
        res, first_binary = [0], 1
        for i in range(0, n):
            for j in range(len(res) - 1, -1, -1):
                res.append(first_binary + res[j])
            first_binary = first_binary << 1
        return res


if __name__ == "__main__":
    n = 3
    result = Solution().grayCode(n)
    print("result: {}".format(result))
