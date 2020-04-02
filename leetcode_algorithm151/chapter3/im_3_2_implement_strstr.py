class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 24 ms
        # 13.2 MB
        return haystack.find(needle)

    def strStr2(self, haystack, needle):
        # sunday 算法
        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st)-1,-1,-1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st)-i
            dic["ot"] = len(st)+1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack):return -1
        if needle=="": return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx+len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx+len(needle)]

            # 判断是否匹配
            if str_cut==needle:
                return idx
            else:
                # 边界处理
                if idx+len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx+len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx+len(needle) >= len(haystack) else idx

    def strStr3(self, haystack, needle):
        # 68 ms
        # 15 MB
        def kmp(needle):
            j = -1
            i = 0
            b = [0 for i in range(0, len(needle) + 1)]
            b[i] = j
            while i < len(needle):
                while j >= 0 and needle[i] != needle[j]:
                    j = b[j]
                i += 1
                j += 1
                b[i] = j
            return b
        if needle == "":
            return 0
        b = kmp(needle)
        print(b)
        j = 0
        i = 0
        while j < len(haystack):
            while i >= 0 and needle[i] != haystack[j]:
                i = b[i]
            i +=1
            j += 1
            if i == len(needle):
                return j - len(needle)
        return -1


if __name__ == "__main__":
    # haystack, needle = "hello", "ll"
    # haystack, needle = "aaaaa", "bba"
    haystack, needle = "aaacaaab", "aaab"
    # result = Solution().strStr(haystack, needle)
    result = Solution().strStr3(haystack, needle)
    print("result: {}".format(result))
