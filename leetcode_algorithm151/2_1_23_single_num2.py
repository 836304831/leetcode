class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 20 ms
        # 14 MB
        return (3*sum(set(nums)) - sum(nums))//2

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_once = seen_twice = 0

        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once



if __name__ == "__main__":
    # nums = [2, 2, 3, 2]
    nums = [0, 1, 0, 1, 0, 1, 99]

    result = Solution().singleNumber2(nums)
    print("result: {}".format(result))
