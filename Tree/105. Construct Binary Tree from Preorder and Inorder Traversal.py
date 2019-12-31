"""
据前序遍历得到根节点，在中序遍历中找到根节点的值所在的位置，
该位置之前为左子树的中序遍历序列，该位置之后为右子树的中序遍历序列，
递归生成左子树和右子树即可。

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 找到根在中序中的位置
        x = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:x + 1], inorder[:x])
        # 构建右子树
        root.right = self.buildTree(preorder[x + 1:], inorder[x + 1:])

        return root



