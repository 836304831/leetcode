

class Stack(object):
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def peek(self):
        if self.is_Empty():
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 76 ms
        # 14.5 MB
        ans = 0
        stack = Stack()
        for i in range(0, len(s)):
            if s[i] == "(" or stack.is_Empty():
                stack.push((s[i], i))
                continue

            ch, index = stack.peek()
            if ch == "(" and s[i] == ")":
                stack.pop()
                if stack.is_Empty() and i + 1 > ans:
                    ans = i + 1
                else:
                    ch, index = stack.peek()
                    if i - index > ans:
                        ans = i - index
            else:
                stack.push((s[i], i))
        return ans

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 测试用例：s = "(()())"  # 正确结果为6， 本地测试用例通过，提交不通过
        ans = 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2 if i > 2 else 2
                elif i - dp[i-1] - 1 and s[i - dp[i-1] - 1] == "(":
                    dp[i] = dp[i - dp[i-1] - 2] + dp[i - 1] + 2 if i - dp[i-1] - 2 > 0 else 2 + dp[i-1]

                ans = max(ans, dp[i])
        return ans


if __name__ == "__main__":

    # s = "(()"
    # s = ")()())"
    # s = "()(()"
    # s = "()"
    # s = "()(()"
    # s = ")()())"    # 4
    s = "(()())"  # 6
    result = Solution().longestValidParentheses(s)
    print("result: {}".format(result))
