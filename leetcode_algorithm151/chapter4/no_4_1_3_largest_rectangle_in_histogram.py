
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
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        stack = Stack()
        for i in range(0, len(heights)):
            if stack.is_Empty() or heights[stack.peek()] <= heights[i]:
                stack.push(i)
                continue

            while not stack.is_Empty() and heights[stack.peek()] >= heights[i]:
                idx = stack.pop()
                ans = max(ans, (i - idx) * heights[idx])
            stack.push(i)

        last_index = -1
        while not stack.is_Empty():
            last_index = stack.peek()
            ans = max(ans, heights[last_index] * (len(heights) - last_index))
            stack.pop()
        if last_index != -1:
            ans = max(ans, heights[last_index] * (len(heights)))

        return ans


if __name__ == "__main__":
    # heights = [2, 1, 5, 6, 2, 3]  # 10
    # heights = [1, 1, 2, 4, 2, 3]  # 6
    # heights = [2, 1, 2]
    # heights = [3, 2, 1, 2, 3]
    heights = [5, 4, 1, 2]  # 5
    result = Solution().largestRectangleArea(heights)
    print("result: {}".format(result))
