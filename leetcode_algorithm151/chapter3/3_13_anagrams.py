class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 96 ms
        # 16.7 MB
        ans_map = {}
        for i in range(0, len(strs)):
            single_str = strs[i]
            single_str = "".join(sorted(single_str))
            if ans_map.__contains__(single_str):
                ans_map.get(single_str).append(strs[i])
            else:
                ans_map[single_str] = [strs[i]]
        ans_list = []
        for key in ans_map.keys():
            ans_list.append(ans_map[key])
        return ans_list


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print("result:{}".format(result))
