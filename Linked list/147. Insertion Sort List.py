"""
插入排序本身的思想：
就是将数组分为两部分，前部分为已排序数组，后部分为未排序数组
每次从未排序数组中取出一个元素，在已排序数组中找到元素插入的位置

排序过程：
1、需要一个指针指向当前已排序的最后一个位置
2、需要另外一个指针每次从表头循环
3、每次拿出未排序的节点，和前驱比较，如果大于或者等于前驱，直接进入下一次循环
      如果前驱小，则进入内层循环比较，插入对应位置即可。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummpHead = ListNode(0)
        dummpHead.next = head

        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
                continue

            pre = dummpHead

            while pre.next.val < head.next.val:
                pre = pre.next

            tmp = head.next
            # 更新 head.next
            head.next = tmp.next

            tmp.next = pre.next
            pre.next = tmp

        return dummpHead.next
