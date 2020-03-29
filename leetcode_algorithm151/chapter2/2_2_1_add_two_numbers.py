# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 76 ms
        # 12.8 MB
        c = 0
        head = l1
        last_node = None
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + c
            c = value // 10
            l1.val = value % 10
            last_node = l1
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            value = l1.val + c
            c = value // 10
            l1.val = value % 10
            last_node = l1
            l1 = l1.next
        while l2 is not None:
            value = l2.val + c
            c = value // 10
            l2.val = value % 10
            last_node.next = l2
            last_node = last_node.next
            l2 = l2.next
        if l1 is None and l2 is None and c != 0:
            last_node.next = ListNode(c)
        return head


def generate_linkblock(nums):
    head = None
    tail = None
    for i in range(0, len(nums)):
        node = ListNode(nums[i])
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = tail.next
    return head


def print_linkblock(head):
    print_p = head
    result = ""
    while print_p is not None:
        result += str(print_p.val) + "->"
        print_p = print_p.next
    print(result)


if __name__ == "__main__":
    nums1, nums2 = [2, 4, 3], [5, 6, 7, 9]
    l1 = generate_linkblock(nums1)
    l2 = generate_linkblock(nums2)
    print_linkblock(l1)
    print_linkblock(l2)
    result = Solution().addTwoNumbers(l1, l2)
    print_linkblock(result)
