# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/5/15 7:50 下午
# @Author  : changqingai
# @FileName: 52_get_intersection_node.py
# ----------------------------


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        # 188 ms	29.7 MB
        if headA is None or headB is None:
            return None
        a_len = self._link_len(headA)
        b_len = self._link_len(headB)

        if a_len > b_len:
            a_link = headA
            b_link = headB
            diff = a_len - b_len
        else:
            a_link = headB
            b_link = headA
            diff = b_len - a_len

        # move first
        while diff > 0:
            a_link = a_link.next
            diff -= 1

        while a_link is not None:
            if a_link == b_link:
                return a_link
            a_link = a_link.next
            b_link = b_link.next

        return a_link

    def _link_len(self, p):
        a_len = 0
        while p is not None:
            a_len += 1
            p = p.next
        return a_len

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
    nums1 = [4, 1, 8, 4, 5]
    nums2 = [5, 0, 1, 8, 4, 5]
    # nums1, m, n = [1], 1, 1
    head_a = generate_linkblock(nums1)
    head_b = generate_linkblock(nums2)

    print_linkblock(head_a)
    result = Solution().getIntersectionNode(head_a, head_b)
    print_linkblock(result)
