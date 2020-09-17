# !/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2020/9/17 下午9:01
# @Author  : changqingai
# @FileName: leetcode_24_Swap_Nodes_in_Pairs.py
# ----------------------------


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """ 	28 ms	12.5 MB"""
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            node = head.next
            node.next = head
            head.next = None
            return node

        tmp_head = head.next
        prepre_p = None
        pre_p = head
        tail_p = pre_p.next
        while tail_p is not None:
            node = tail_p.next
            pre_p.next = node
            tail_p.next = pre_p
            if prepre_p is None:
                prepre_p = tail_p
            else:
                prepre_p.next = tail_p
            prepre_p = pre_p
            if node is None:
                pre_p = None
                tail_p = None
                continue
            pre_p = node
            tail_p = pre_p.next
        return tmp_head


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    l1 = generate_linkblock(nums)

    print_linkblock(l1)
    result = Solution().swapPairs(l1)
    print_linkblock(result)
