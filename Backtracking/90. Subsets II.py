"""
我们只需要判断当前数字和上一个数字是否相同，相同的话跳过即可。当然，要把数字首先进行排序。
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 排序
        nums.sort()
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, start, path, res):
        res.append(path[:])

        for i in range(start, len(nums)):
            # 和上一个数字相等就跳过去
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.helper(nums, i + 1, path, res)
            path.pop()
