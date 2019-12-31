"""
一般的二叉搜索树是左<=根<右，而这道题设定为左<根<右，那么就可以用中序遍历来做。
判断中序遍历序列是否为递增序列。

"""

# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        stack = []
        inorder = float('-inf')  # 负无穷
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            tmp = stack.pop()
            if tmp.val <= inorder:
                return False
            inorder = tmp.val
            node = tmp.right

        return True
