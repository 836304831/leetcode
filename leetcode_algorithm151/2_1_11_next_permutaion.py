
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 24 ms, 12.9 MB
        split_index = -1
        for i in range(len(nums) - 1, -1, -1):
            if i > 0 and nums[i] > nums[i - 1]:
                split_index = i - 1
                break
        if split_index != -1:
            target = nums[split_index]
            big_index = self.find_big_index(nums, split_index + 1, len(nums) - 1, target)
            nums[split_index] = nums[big_index]
            nums[big_index] = target
            self.swap(nums, split_index + 1, len(nums) - 1)
            return

        self.swap(nums, 0, len(nums) - 1)
        if nums[0] == 0:
            for i in range(0, len(nums) - 1):
                if nums[i] != 0 and i > 0:
                    tmp = nums[i]
                    nums[i] = 0
                    nums[0] = tmp
                    return

    def swap(self, nums, i, j):
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

    def find_big_index(self, nums, left, right, target):
        for i in range(right, left - 1, -1):
            if nums[i] > target:
                return i


if __name__ == "__main__":
    nums = [1, 2, 3]
    # nums = [1, 2, 0, 0]
    # nums = [1, 1, 5]
    # nums = [2, 1, 0, 0]
    # nums = [1, 3, 2]
    # nums = [3, 2, 1]
    result = Solution().nextPermutation(nums)
    print("result: {}".format(nums))
