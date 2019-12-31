"""
展开的顺序其实就是二叉树的先序遍历。
步骤：
（1）将左子树插入到右子树的地方
（2）将原来的右子树接到左子树的最右边节点
（3）考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                pre = root.left
                # 找到左子树中的最右节点
                while pre.right:
                    pre = pre.right
                # 将左子树中的最右节点的右子树指向根节点的右子树
                pre.right = root.right
                # 将左子树插入右子树的地方
                root.right = root.left
                # 左子树置空
                root.left = None

            # 继续下一个节点
            root = root.right

        return