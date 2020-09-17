# !/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2020/9/17 下午5:50
# @Author  : changqingai
# @FileName: leetcode_19_Remove_Nth_Node_End_List.py
# ----------------------------

# Definition for singly-linked list.


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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """24 ms	12.3 MB"""
        tail = head
        tmp_head = head
        has_n_node = True
        for i in range(0, n):
            if tail is None:
                has_n_node = False
                break
            tail = tail.next
        if not has_n_node:
            return None

        prepre_p = None
        pre_p = head
        while tail is not None:
            tail = tail.next
            prepre_p = pre_p
            pre_p = pre_p.next
        if prepre_p is None:
            return pre_p.next

        prepre_p.next = pre_p.next
        return tmp_head


if __name__ == "__main__":
    nums, n = [1, 2, 3, 4, 5], 5
    l1 = generate_linkblock(nums)

    print_linkblock(l1)
    result = Solution().removeNthFromEnd(l1, n)
    print_linkblock(result)
