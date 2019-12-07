"""
回溯搜索”算法即“深度优先遍历 + 状态重置 + 剪枝”。

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == None:
            return []

        used = [False ] *len(nums)
        res = []
        self.helper(nums ,0 ,[] ,used ,res)
        return res

    def helper(self, nums, index, path, used, res):
        if index == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self.helper(nums ,index +1 ,path ,used ,res)
                used[i] = False
                path.pop()