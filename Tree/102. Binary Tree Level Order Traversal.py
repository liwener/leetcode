"""
通用写法。可以方便定位到每一个层特定的的元素。
"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res

        queue = [root]
        while queue:
            # 使用列表存储同层结点
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                tmp.append(node.val)
            res.append(tmp)

        return res
