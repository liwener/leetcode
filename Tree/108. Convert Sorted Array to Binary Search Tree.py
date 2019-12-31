"""
二叉树中序遍历的逆过程
递归+二分：与二分的思路完全一样

"""


# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        l, r = 0, len(nums) - 1
        mid = l + (r -l)>>1

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[l:mid])
        root.right = self.sortedArrayToBST(nums[mid +1:r +1])

        return root