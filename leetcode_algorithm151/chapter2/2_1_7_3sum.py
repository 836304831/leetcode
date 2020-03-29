class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 632 ms	18.2 MB
        result = []
        if nums is None or len(nums) < 3:
            return result
        nums.sort(key=lambda x: x)
        for idx in range(0, len(nums)):
            if nums[idx] > 0:
                continue
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                if nums[idx] + nums[left] + nums[right] == 0:
                    result.append([nums[idx], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[idx] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return result


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [0, 0, 0, 0]
    # nums = [1, -1, -1, 0]
    result = Solution().threeSum(nums)
    print("result: {}".format(result))
