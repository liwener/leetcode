"""
建立两个链表实现，一个所有值小于x，一个所有值大于等于x。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        p1 = ListNode(0)
        p2 = ListNode(0)
        dummyHead1 = p1
        dummyHead2 = p2

        while head:
            if head.val < x:
                p1.next =head
                p1 = p1.next
            else:
                p2.next =head
                p2 = p2.next
            head = head.next

        p1.next = dummyHead2.next
        p2.next = None

        return dummyHead1.next


