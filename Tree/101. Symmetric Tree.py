"""
如果同时满足下面的条件，两个树互为镜像：
（1）它们的两个根结点具有相同的值。
（2）每个树的右子树都与另一个树的左子树镜像对称。

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1== None and t2== None:
            return True
        if t1 != None and t2 != None and t1.val == t2.val:
            return self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

        else:
            return False







