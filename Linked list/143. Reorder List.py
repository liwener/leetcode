"""
三步：
1、快慢指针找到中点
2、拆成两个链表
3、拼接两个链表

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head

        slow = fast = head
        # 找到链表中点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        p = slow.next
        slow.next = None

        cur = None
        # 后部分反转
        while p:
            tmp = p.next
            p.next = cur
            cur = p
            p = tmp

        # 连接两个链表
        pre = head

        while pre and cur:
            tmp1 = pre.next
            tmp2 = cur.next

            pre.next = cur
            cur.next = tmp1

            pre = tmp1
            cur = tmp2

        return head