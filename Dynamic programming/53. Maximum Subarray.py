"""
动态规划：
(1)第i个元素结尾且和最大的连续子数组，要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素，要么是只包含第i个元素。
(2)以第i个数为结束点的子数列的最大和，存在一个递推关系:sum[i] = max(sum[i-1] + a[i], a[i]),等价于判断sum[i-1]是否大于0。每次运算只需要前一次的结果。
(3)将这些最大和保存下来后，取最大。

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tal = 0

        for i in range(len(nums)):
            # 求以第i个数为结束点的子数列的最大和
            if tal > 0:
                tal += nums[i]
            else:
                tal = nums[i]

            # 取最大的那个
            if tal > res:
                res = tal

        return res