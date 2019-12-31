"""
在遍历时要记录val,
当root是叶节点时，如果root值 等于 剩余值时，说明形成一条正确的路径。
其它情况，剩余值减去root值，递归到左子树和右子树。
"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def helper(root, sum, path):
            if not root:
                return
                # 访问叶子节点
            if not root.left and not root.right and sum - root.val == 0:
                path += [root.val]  # 缓存路径中的数据
                res.append(path)
                return

            helper(root.left, sum - root.val, path +[root.val])
            helper(root.right, sum - root.val, path+ [root.val])

        helper(root, sum, [])
        return res

