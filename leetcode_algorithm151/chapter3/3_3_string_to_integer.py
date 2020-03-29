class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 40 ms
        # 12.7 MB
        int_max = "2147483647"
        int_min = "-2147483648"
        i = 0
        j = 0
        for i in range(0, len(str)):
            if str[i] != " ":
                break

        # for j in range(i, len(str)):
        #     if str[j] != "0":
        #         break
        # i = j
        if i == len(str):
            return 0
        num_str = ""
        if str[i] == "+" or str[i] == "-":
            num_str = str[i]
            i += 1

        for j in range(i, len(str)):
            if str[j] != "0":
                break
        i = j
        for j in range(i, len(str)):
            if not str[j].isdecimal():
                break
            num_str += str[j]
        if num_str == "" or (len(num_str) == 1 and (num_str[0] == "+" or num_str[0] == "-")):
            return 0
        if num_str[0] == "-":
            if len(num_str) > len(int_min):
                return int(int_min)
            elif len(num_str) == len(int_min):
                num_str = int_min if num_str > int_min else num_str
            return int(num_str)
        num_str = num_str[1:] if num_str[0] == "+" else num_str
        if len(num_str) > len(int_max):
            return int(int_max)
        elif len(num_str) == len(int_max):
            num_str = int_max if num_str > int_max else num_str
        return int(num_str)


if __name__ == "__main__":

    # str = "42"
    # str = "   -42"
    # str = "4193 with words"
    # str = "words and 987"
    # str = "-91283472332"
    str = "  0000000000012345678"
    # str = "0-1"
    result = Solution().myAtoi(str)
    print("result: {}".format(result))