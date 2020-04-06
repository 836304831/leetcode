class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 24 ms
        # 12.8 MB
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        shortest_len = len(strs[0])
        for i in range(1, len(strs)):
            if shortest_len > len(strs[i]):
                shortest_len = len(strs[i])
        i = 0
        while i < shortest_len:
            ch = strs[0][i]
            flag = True
            for j in range(1, len(strs)):
                if ch != strs[j][i]:
                    flag = False
                    break
            if not flag:
                break
            i += 1
        return strs[0][0:i]


if __name__ == "__main__":
    # strs = ["flower", "flow", "flight"]
    strs = ["dog", "rececar", "car"]
    # strs = ["a"]
    # strs = ["c", "c"]
    result = Solution().longestCommonPrefix(strs)
    print("result:{}".format(result))
