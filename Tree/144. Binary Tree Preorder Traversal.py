"""
因为要在遍历完节点的左子树后接着遍历节点的右子树，为了能找到该节点，需要使用栈来进行暂存。中序和后序也都涉及到回溯，所以都需要用到栈。
对于任一结点P：
（1）访问结点P，并将结点P入栈;
（2）判断结点P的左孩子是否为空。若为空，则栈顶结点出栈，并将栈顶结点的右孩子置为当前的结点P，循环至（1）;若不为空，则将P的左孩子置为当前的结点P;
（3）直到P为NULL或者栈为空，则遍历结束。

"""
# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        node = root
        while node or stack:
            # 从根节点开始，一直找它的左子树
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left

            node = stack.pop()
            # 开始查找它的右子树
            node = node.right

        return res