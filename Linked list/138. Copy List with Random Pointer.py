"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        node = head
        # 将克隆结点放在原结点后面
        while node:
            clone = Node(node.val, node.next, None)
            tmp = node.next
            node.next = clone
            node = tmp

        node = head
        # 处理random指针
        while node:
            if node.random != None:
                node.next.random = node.random.next
            node = node.next.next

        # 分离原链表和克隆链表
        node = head
        CloneHead = head.next
        while node and node.next:
            tmp = node.next
            node.next = node.next.next
            node = tmp

        return CloneHead
