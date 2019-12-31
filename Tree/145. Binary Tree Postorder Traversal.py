"""
后序遍历中，要保证左孩子和右孩子都已被访问并且左孩子在右孩子前访问才能访问根结点。

"""

# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        # 这个while循环的功能是找出后序遍历的逆序
        while stack1:
            node = stack1.pop()

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

            stack2.append(node)

        while stack2:
            res.append(stack2.pop().val)

        return res




