class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 2556 ms
        # 13.8 MB
        if len(gas) == 0 and len(cost) == 0:
            return -1
        gas_len = len(gas)
        for start_index in range(0, gas_len):
            cur_gas = gas[start_index]
            for j in range(start_index, start_index + gas_len):
                cur_gas = cur_gas - cost[j % gas_len]
                if cur_gas < 0:
                    break
                cur_gas += gas[(j + 1) % gas_len]
            if cur_gas >= 0:
                return start_index
        return -1


if __name__ == "__main__":
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    gas = [2, 3, 4]
    cost = [3, 4, 3]

    # gas = [5, 1, 2, 3, 4]
    # cost = [4, 4, 1, 5, 1]
    result = Solution().canCompleteCircuit(gas, cost)
    print("result: {}".format(result))
