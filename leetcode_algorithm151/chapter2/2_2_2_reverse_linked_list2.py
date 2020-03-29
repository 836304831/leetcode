# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 24 ms
        # 13 MB
        if head is not None and head.next is None:
            return head

        raw_head = None
        raw_tail = None

        reverse_head = None
        reverse_tail = None

        count = 0
        cur_p = head
        while cur_p is not None:
            next_cur_p = cur_p.next
            count += 1
            if count < m:
                if raw_head is None:
                    raw_head = cur_p
                    raw_tail = cur_p

                    raw_head.next = None
                    raw_tail.next = None
                else:
                    raw_tail.next = cur_p
                    raw_tail = raw_tail.next
                    raw_tail.next = None
            elif m <= count <= n:
                if reverse_head is None:
                    reverse_head = cur_p
                    reverse_tail = cur_p
                    reverse_head.next = None
                    reverse_tail.next = None
                else:
                    cur_node = cur_p
                    cur_node.next = reverse_head
                    reverse_head = cur_node

            else:
                reverse_tail.next = cur_p
                break
            cur_p = next_cur_p
        if raw_head is None:
            raw_head = reverse_head
        else:
            raw_tail.next = reverse_head
        return raw_head


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
    nums1, m, n = [1, 2, 3, 4, 5], 2, 4
    # nums1, m, n = [1], 1, 1
    head = generate_linkblock(nums1)
    print_linkblock(head)
    result = Solution().reverseBetween(head, m, n)
    print_linkblock(result)
