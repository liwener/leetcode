"""
解法：递归
临界条件：最近公共祖先为根节点
根节点是空节点、q节点、p节点

求解:从左右子树分别进行递归，即查找左右子树上是否有p节点或者q节点
（1）左、右子树均能找到,说明此时的p节点和q节点在当前root节点两侧，返回root节点
（2）左子树找到，右子树没有找到，返回左子树的查找结果
（3）右子树找到，左子树没有找到，返回右子树的查找结果

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 左、右子树均能找到
        if left != None and right != None:
            return root

        return left if left != None else right
