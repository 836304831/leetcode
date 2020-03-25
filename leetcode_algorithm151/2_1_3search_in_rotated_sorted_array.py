class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 8 ms 11.8 MB
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if mid + 1 < len(nums) and nums[mid+1] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        if start > end:
            return -1


if __name__ == "__main__":
    # nums, target = [4, 5, 6, 7, 0, 1, 2], 0
    # nums = []
    nums, target = [3, 1], 1

    index = Solution().search(nums, target)
    print("index: {}".format(index))
