"""
主要在于“摘链”和“链接”的操作。

 实现思路 ：以1->2->3->4->5, m = 2, n=4 为例:
（1）定位到要反转部分的头节点 2，head = 2；前驱结点 1，pre = 1；
（2）当前节点的下一个节点3调整为前驱节点的下一个节点 1->3->2->4->5,
（3）当前结点仍为2， 前驱结点依然是1，将3与2看作一个整体，重复上述操作，不断增加整体的长度。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead

        for i in range(m - 1):
            pre = pre.next

        cur = pre.next

        for i in range(m, n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        return dummyHead.next





