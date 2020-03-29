class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 32 ms 12.9 MB
        if len(digits) == 0:
            return digits
        digits[len(digits) - 1] += 1
        c = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += c
            c = digits[i] // 10
            digits[i] = digits[i] % 10
        if c != 0:
            digits.insert(0, c)
        return digits


if __name__ == "__main__":
    # nums = [4, 3, 2, 1]
    # nums = [1, 2, 3]
    nums = [9, 9]
    result = Solution().plusOne(nums)
    print("result: {}".format(result))
