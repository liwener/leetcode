# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        l_height = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)

        return max(l_height, r_height) + 1
