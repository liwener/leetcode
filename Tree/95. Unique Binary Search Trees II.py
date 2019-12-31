"""
如果将 i 作为跟节点，那么 [1, i) 为 i 的左子树节点，(i, n] 为右子树节点。

问题就被拆分为两个子问题了：
求左子树的所有排列，求右子树的所有排列

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, left, right):
        res = []
        if left > right:
            return [None]

        for i in range(left, right + 1):  # 找个根节点
            left_node = self.helper(left, i - 1)
            right_node = self.helper(i + 1, right)
            # 从根节点左右各找一个左子树和右子树
            for l in left_node:
                for r in right_node:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)

        return res