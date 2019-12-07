"""
循环旋转，本质是将尾部向前第K个元素作为头
方法：先把链表首尾相连，再找到位置断开循环
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return head

        cur = end = head
        n = 1
        while end.next:
            end = end.next
            n += 1
        # 形成循环链表
        end.next = head

        # 得到需要切断的位置
        pos = n - (k % n)
        # head本身算1个
        while pos > 1:
            cur = cur.next
            pos -= 1

        p = cur.next
        cur.next = None

        return p