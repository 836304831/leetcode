
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
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 28 ms
        # 12.8 MB
        if s == "":
            return True
        i, j = 0, 0
        stack = Stack()
        while j < len(s):
            if s[j] == "(" or s[j] == "[" or s[j] == "{":
                stack.push(s[j])
                j += 1
                continue
            if stack.is_Empty():
                return False
            ch = stack.pop()
            if (s[j] == ")" and ch == "(") or (s[j] == "]" and ch == "[") or (s[j] == "}" and ch == "{"):
                j += 1
                continue
            else:
                return False
        if stack.is_Empty():
            return True
        return False


if __name__ == "__main__":

    # s = "()"
    # s = "()[]{}"
    # s = "(}"
    # s = "([)]"
    s = "{[]}"
    result = Solution().isValid(s)
    print("result: {}".format(result))