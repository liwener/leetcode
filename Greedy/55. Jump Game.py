"""
贪心算法：
       每次选取上一跳中可达范围 i+nums[i]最大的，迭代可达范围，
       当可达范围到达终点时，直接返回true。
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxdist = nums[0]
        i = 0

        while i <= maxdist:
            maxdist = max(i + nums[i], maxdist)
            if maxdist >= (len(nums) - 1):
                return True
            i += 1

        return False