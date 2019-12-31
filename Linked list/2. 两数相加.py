# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummpHead = ListNode(0)
        cur = dummpHead
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = x + y + carry
            cur.next = ListNode(s % 10)
            carry = s // 10  # 跟踪进位
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:  # 表尾溢出
            cur.next = ListNode(1)

        return dummpHead.next



