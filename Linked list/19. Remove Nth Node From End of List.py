"""
思路：双指针法
第一个指针从列表的开头向前移动 n+1步，而第二个指针将从列表的开头出发。
设置虚拟节点,要找的是待删除结点的前一个节点，而 head 有可能是被删掉的点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummp = ListNode(0)
        dummp.next = head
        fast = slow = dummp

        # 直到first到None
        for i in range(n +1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummp.next
