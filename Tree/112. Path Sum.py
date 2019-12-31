"""
深度优先遍历二叉树，每深入一次，sum-根节点的值，
当到达叶子节点的时候，判断sum是否等于当前的节点值,
如果等于，说明找到了，否则尝试另外一条路径。

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val

        # 到达叶子节点的时候，判断sum是否等于当前的节点值
        if not root.left and not root.right:
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)



