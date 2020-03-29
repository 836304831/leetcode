class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 24 ms	13.7 MB
        if nums is None or len(nums) == 0:
            return 0
        num_used_map = dict()
        for idx, num in enumerate(nums):
            num_used_map[num] = False

        longest_len = 1
        for idx, num in enumerate(nums):
            if num_used_map.get(num):
                continue
            current_len = 1
            current_num = num - 1
            num_used_map[num] = True
            while num_used_map.__contains__(current_num):
                num_used_map[current_num] = True
                current_len += 1
                current_num -= 1

            current_num = num + 1
            while num_used_map.__contains__(current_num):
                num_used_map[current_num] = True
                current_len += 1
                current_num += 1

            if current_len > longest_len:
                longest_len = current_len
        return longest_len


if __name__ == "__main__":
    # nums = [100, 4, 200, 1, 3, 2]
    nums = [100, 4, 6, 1, 1, 2, 3, 3, 7, 5]
    result = Solution().longestConsecutive(nums)
    print("result: {}".format(result))
