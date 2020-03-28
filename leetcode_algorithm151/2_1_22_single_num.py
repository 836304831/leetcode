class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 44 ms
        # 14.2 MB
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans


if __name__ == "__main__":
    # nums = [4, 1, 2, 1, 2]
    nums = [2, 2, 1]
    result = Solution().singleNumber(nums)
    print("result: {}".format(result))
