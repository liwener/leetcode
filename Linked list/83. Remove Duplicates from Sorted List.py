"""
将当前结点的值与下一个结点值比较确定是否为重复结点。
如果是，更改当前结点的 next 指针，跳过下一个结点并直接指向下一个结点之后的结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                # 跳过下一个结点，更新cur.next
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head