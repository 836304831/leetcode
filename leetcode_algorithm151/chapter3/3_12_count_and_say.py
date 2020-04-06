class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 20 ms
        # 12.8 MB
        if n == 1:
            return "1"

        raw_str = "1"
        for i in range(1, n):
            new_str = self.next_str(raw_str)
            raw_str = new_str
        return raw_str

    def next_str(self, raw_str):
        new_str = ""
        i = 0
        while i < len(raw_str):
            j = i + 1
            while j < len(raw_str):
                if raw_str[i] == raw_str[j]:
                    j += 1
                else:
                    break
            new_str += str(j - i) + raw_str[i]
            i = j
        return new_str


if __name__ == "__main__":
    n = 5
    result = Solution().countAndSay(n)
    print("result:{}".format(result))
