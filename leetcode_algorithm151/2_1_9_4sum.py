
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 736 ms, 12.9 MB
        result = []
        nums = sorted(nums, key=lambda x:x)
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    tmp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left + 1 < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right - 1 > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp_sum > target:
                        right -= 1
                    else:
                        left += 1
        return result


if __name__ == "__main__":
    nums, target = [1, 0, -1, 0, -2, 2], 0
    result = Solution().fourSum(nums, target)
    print("result: {}".format(result))
