"""
根据中序遍历的顺序，对于任一结点，优先访问其左孩子，而左孩子结点又可以看做根结点，然后继续访问其左孩子结点，
直到遇到左孩子结点为空的结点才进行访问，然后按相同的规则访问其右子树。

非递归实现,对于任一结点P：
  1)若其左孩子不为空，则将P入栈并将P的左孩子置为当前的P，然后对当前结点P再进行相同的处理；
  2)若其左孩子为空，则取栈顶元素并进行出栈操作，访问该栈顶结点，然后将当前的P置为栈顶结点的右孩子；
  3)直到P为NULL并且栈为空则遍历结束

"""

# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        node = root
        stack = []
        res = []

        while node or stack:
            # 从根结点开始，寻找左子树，把它压入栈中
            while node:
                stack.append(node)
                node = node.left

            # while 结束代表前一个节点没有了左子树
            tmp = stack.pop()
            res.append(tmp.val)
            node = tmp.right

        return res

