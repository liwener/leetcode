"""
快慢指针:
 h -> 1 -> 2    3    3 -> 4 -> 4 -> 5 -> 6
           |              |
           ------------————
          slow           fast
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummpHead = ListNode(0)
        dummpHead.next = head

        fast = head
        slow = dummpHead

        while fast:
            duplicate = False
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
                duplicate = True
            # 不存在重复元素
            if duplicate == False:
                slow = fast
            # 存在重复元素
            else:
                slow.next = fast.next

            fast = fast.next

        return dummpHead.next

