"""
归并排序：
1、快慢指针找中点
2、递归调用mergeSort
3、合并两个链表

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        else:
            return self.mergeSort(head)

    def mergeSort(self ,head):
        if head.next == None:
            return head

        # 找到链表中点
        # fast要比slow先走一步,这样最终确定slow即为中值
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cut = slow.next
        slow.next = None

        l = self.mergeSort(head)
        r = self.mergeSort(cut)
        return self.merge(l, r)

    # 合并两个有序链表
    def merge(self, l, r):
        dummyHead = ListNode(0)
        cur = dummyHead

        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next

            else:
                cur.next = r
                r = r.next
            cur = cur.next

        if l:
            cur.next = l
        if r:
            cur.next = r

        return dummyHead.next