"""
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

这道题的关键是搞清楚递归结束条件：
叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
当 root 节点左右孩子都为空时，返回 1
当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 左孩子和右孩子都为空
        if not root.left and not root.right:
            return 1

        m1 = self.minDepth(root.left)
        m2 = self.minDepth(root.right)

        # 左孩子和右孩子有一个为空
        if not root.left or not root.right:
            return m1 + m2 + 1
        # 左右孩子都不为空，返回最小深度+1
        return min(m1, m2) + 1

        return min(left, right) + 1