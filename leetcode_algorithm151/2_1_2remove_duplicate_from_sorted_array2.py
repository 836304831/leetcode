class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 20 ms 11.7 MB
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        num_len = 0
        for idx in range(1, len(nums)):
            if nums[num_len] == nums[idx]:
                if num_len >= 1:
                    if nums[num_len - 1] != nums[idx]:
                        num_len += 1
                        nums[num_len] = nums[idx]
                else:
                    num_len += 1
                    nums[num_len] = nums[idx]

            else:
                num_len += 1
                nums[num_len] = nums[idx]
        return num_len + 1


if __name__ == "__main__":
    # nums = [1, 1, 1, 2, 2, 3]
    nums = [1, 2]
    num_len = Solution().removeDuplicates(nums)
    print("num_len: {}, nums: {}".format(num_len, nums))
