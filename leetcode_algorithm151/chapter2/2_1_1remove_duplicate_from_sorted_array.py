class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 36 ms 13.1 MB
        if len(nums) == 0:
            return 0

        num_len = 0
        for idx, value in enumerate(nums):
            if nums[num_len] != value:
                num_len += 1
                nums[num_len] = value
        return num_len + 1

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 3876 ms 13.7 MB
        num_len = 0
        idx = 0
        while idx < len(nums):
            value = nums[idx]
            num_len += 1
            for idx2 in range(idx + 1, len(nums)):
                if nums[idx2] == value:
                    idx += 1
            idx += 1
            if idx < len(nums):
                nums[num_len] = nums[idx]
        return num_len


if __name__ == "__main__":
    nums = [1, 1, 2]
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    num_len = Solution().removeDuplicates(nums)
    print("num_len: {}, nums: {}".format(num_len, nums))
