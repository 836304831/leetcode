
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
    def evalRPN(self, tokens):
        """
        :type s: str
        :rtype: bool
        """
        # 52 ms
        # 13.9 MB
        ans = 0
        if len(tokens) == 0:
            return ans
        op_map = {"+": self.plus, "-": self.minus, "*": self.multi, "/": self.divide}
        stack = Stack()
        for i in range(0, len(tokens)):
            if op_map.__contains__(tokens[i]):
                b = stack.pop()
                a = stack.pop()
                stack.push(op_map.get(tokens[i])(a, b))
            else:
                stack.push(tokens[i])
        return stack.pop()

    def plus(self, a, b):
        return int(a) + int(b)

    def minus(self, a, b):
        return int(a) - int(b)

    def multi(self, a, b):
        return int(a) * int(b)

    def divide(self, a, b):
        return int(int(a) / int(b))


if __name__ == "__main__":

    # tokens = ["2", "1", "+", "3", "*"]
    # tokens = ["4", "13", "5", "/", "+"]
    # tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = Solution().evalRPN(tokens)
    print("result: {}".format(result))
