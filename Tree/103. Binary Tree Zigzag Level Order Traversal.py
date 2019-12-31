"""
设置一个bool型的变量，每次判断是该从左往右，还是从右往左即可。
然后每遍历一层，对这个bool型变量取反。
"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res

        queue = [root]
        flag = True

        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)

            if flag:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            flag = not flag

        return res

