class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid]:
                start += 1
                continue
            if nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if mid + 1 < len(nums) and nums[mid + 1] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        if start > end:
            return False


if __name__ == "__main__":
    # nums, target = [2, 5, 6, 0, 0, 1, 2], 0
    # nums, target = [2, 5, 6, 0, 0, 1, 2], 3
    # nums, target = [1, 3, 1, 1, 1, 1, 1], 3
    # nums, target = [3, 1], 1
    nums, target = [5, 1, 3], 3

    result = Solution().search(nums, target)
    print("result: {}".format(result))
