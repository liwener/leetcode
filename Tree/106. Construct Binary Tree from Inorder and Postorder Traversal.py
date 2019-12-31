"""
先要知道一个结论，前序/后序+中序序列可以唯一确定一棵二叉树，所以自然而然可以用来建树。
从前序与中序遍历序列构造二叉树思路一致，区别在于先构建子树的右子树，再构建其左子树。

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        # 确定中序中根的引索，以划分区间
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index +1:], postorder[index:-1])

        return root




