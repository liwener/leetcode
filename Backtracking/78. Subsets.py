"""
组合问题，按顺序读字符，不需要设置 used 数组；
在根结点、非叶子结点和叶子结点都需要结算。

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, array, start, path, res):
        res.append(path[:])

        for i in range(start, len(array)):
            path.append(array[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.helper(array, i+1, path, res)
            path.pop()


