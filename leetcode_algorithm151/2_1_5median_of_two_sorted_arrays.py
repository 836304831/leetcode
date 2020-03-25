class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 执行用时：52 ms
        # 内存消耗：13.7 MB
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2
        if len(nums1) == 0 and len(nums2) == 0:
            return -1
        if len(nums1) == 0:
            return (nums2[len(nums2)//2 - 1] + nums2[len(nums2) // 2]) / 2 if len(nums2) % 2 == 0 else nums2[len(nums2) // 2]

        s1 = 0
        e1 = len(nums1)
        half_k = (len(nums1) + len(nums2) + 1) // 2
        while s1 < e1:
            m1 = s1 + (e1 - s1) // 2
            m2 = half_k - m1
            if nums1[m1] < nums2[m2-1]:
                s1 = m1 + 1
            else:
                e1 = m1
        m1 = s1
        m2 = half_k - m1
        sum_len = len(nums1) + len(nums2)
        max_value = max(nums2[m2 - 1] if m2 - 1 >= 0 else float("-inf"), nums1[m1 - 1] if m1 - 1 >= 0 else float("-inf"))

        if sum_len % 2 == 0:
            min_value = min(nums1[m1] if m1 < len(nums1) else float("inf"), nums2[m2] if m2 < len(nums2) else float("inf"))
            return (min_value + max_value) / 2
        else:
            return max_value

    def findMedianSortedArrays2(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            nums2, nums1 = nums1, nums2
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2


if __name__ == "__main__":
    # nums1, nums2 = [1, 3, 4, 5], []
    # nums1, nums2 = [3, 4, 5], [1, 2]
    # nums1, nums2 = [1, 2], [3, 4]
    # nums1, nums2 = [1, 3], [2]
    nums1, nums2 = [-1, 1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12, 14, 16]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print("result: {}".format(result))
