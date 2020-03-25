import math

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 	676 ms	12.7 MB
        if nums is None or len(nums) < 3:
            return 0
        nums.sort(key=lambda x: x)
        result = nums[0] + nums[1] + nums[2]
        for idx in range(0, len(nums) - 2):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                tmp_sum = nums[idx] + nums[left] + nums[right]
                if math.fabs(tmp_sum - target) < math.fabs(result - target):
                    result = tmp_sum
                if tmp_sum < target:
                    left += 1
                else:
                    right -= 1
        return result


if __name__ == "__main__":
    nums, target = [-1, 2, 1, -4], 1
    result = Solution().threeSumClosest(nums, target)
    print("result: {}".format(result))
