class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 40 ms, 12.7 MB
        count = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[right] == val:
                count += 1
                right -= 1
                continue
            if nums[left] == val:
                count += 1
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return len(nums) - count


if __name__ == "__main__":
    # nums, val = [3, 2, 2, 3], 3
    # nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
    nums, val = [1], 1
    result = Solution().removeElement(nums, val)
    print("result: {}".format(result))
