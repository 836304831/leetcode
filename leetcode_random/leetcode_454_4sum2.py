
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        count = 0
        ab_map = dict()
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                ab = A[i] + B[j]
                if ab_map.__contains__(ab):
                    ab_map[ab] += 1
                else:
                    ab_map[ab] = 1
        for m in range(0, len(C)):
            for n in range(0, len(D)):
                cd = C[m] + D[n]
                if ab_map.__contains__(-cd):
                    count += ab_map[-cd]
        return count


if __name__ == "__main__":
    # A = [1, 2]
    # B = [-2, -1]
    # C = [-1, 2]
    # D = [0, 2]

    A = [0, 1, -1]
    B = [-1, 1, 0]
    C = [0, 0, 1]
    D = [-1, 1, 1]

    result = Solution().fourSumCount(A, B, C, D)
    print("result: {}".format(result))
