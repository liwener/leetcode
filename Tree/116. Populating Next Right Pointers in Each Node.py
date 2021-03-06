"""
层次遍历：使用队列
将每一行的节点加入队列，每次将这一行的节点分别指向右侧节点，同时将左右子节点加入队列
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]

        while queue:
            pre = None
            for i in range(len(queue)):
                cur = queue.pop(0)
                # 前驱节点存在时
                if pre:
                    pre.next = cur
                # 更新前驱节点
                pre = cur

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root



