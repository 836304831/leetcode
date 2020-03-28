class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 36 ms
        # 12.9 MB
        raw_nums = [str(i + 1) for i in range(0, n)]
        product_num_list = self.generate_product(n)
        ans = ""
        k -= 1  # index from 0 start
        while n > 0:
            n -= 1
            product_num = product_num_list[n]
            index = k // product_num

            ans += raw_nums[index]
            raw_nums.remove(raw_nums[index])
            k = k - (product_num * index)
        return ans

    def generate_product(self, n):
        result = []
        result.append(1)
        for i in range(1, n + 1):
            result.append(result[i - 1] * i)
        return result

    def getPermutation2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 28 ms, 12.9 MB
        raw_nums = [i + 1 for i in range(0, n)]
        ans = ""
        k -= 1   # index from 0 start

        while n > 0:
            n -= 1
            product_num = self.product2(n)
            index = k // product_num

            ans += str(raw_nums[index])
            raw_nums.remove(raw_nums[index])
            k = k - (product_num * index)
        return ans

    def product2(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    # n, k = 3, 3
    n, k = 4, 9

    result = Solution().getPermutation(n, k)
    print("result: {}".format(result))
