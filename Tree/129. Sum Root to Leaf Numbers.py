"""
二叉树的题目:递归求解。

先序遍历的变形:
先遍历根节点；再遍历左子树，把走当前路径的数字带到左子树的求解中；
遍历右子树，把走当前路径的数字带到右子树的求解中；
更新总的和。

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.helper(root, 0)

    def helper(self, root, res):
        if not root:
            return 0

        res = res * 10 + root.val

        # 到达叶子节点
        if not root.left and not root.right:
            return res

        # 到达分支
        return self.helper(root.left, res) + self.helper(root.right, res)
