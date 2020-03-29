class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 24 ms
        # 12.6 MB
        ans = 0
        if len(height) == 0:
            return ans
        left, right = 0, len(height) - 1
        his_left_heightest = height[left]
        his_right_heightest = height[right]
        while left < right:
            if height[left] > his_left_heightest:
                his_left_heightest = height[left]
            if height[right] > his_right_heightest:
                his_right_heightest = height[right]
            min_height = min(his_left_heightest, his_right_heightest)
            ans += 0 if min_height < height[left] else min_height - height[left]
            ans += 0 if min_height < height[right] else min_height - height[right]
            if his_left_heightest < his_right_heightest:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == "__main__":
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [0, 0]
    height = []
    result = Solution().trap(height)
    print("result: {}".format(result))
