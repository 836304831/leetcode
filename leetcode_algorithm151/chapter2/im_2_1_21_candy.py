class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 108 ms
        # 14.8 MB
        if len(ratings) == 0:
            return 0
        candy_list = [1 for i in range(0, len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_list[i] = max(candy_list[i], candy_list[i + 1] + 1)
        print(candy_list)
        return sum(candy_list)


if __name__ == "__main__":
    # ratings = [1, 0, 2]
    # ratings = [1, 2, 2]
    ratings = [1, 2, 87, 87, 87, 2, 1]
    result = Solution().candy(ratings)
    print("result: {}".format(result))
