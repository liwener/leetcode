"""
利用二分思想先找其左边界，再找其右边界即可，注意找左边界的时候，由右侧逼近；找右边界的时候，由左侧逼近。
1、尽最大可能排除不符合题意的元素，在每一轮循环中不断减少候选区间的范围，直到候选区间收缩成 1 个数。
2、因为数组中很可能不存在目标值，因此在第 1 步使用“排除法”最后剩下的这个数，再判断一下它是否等于 target 即可。

"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1 ,-1]
        if not nums:
            return res

        l, r = 0, len(nums ) -1
        # 找到起始位置
        while l < r:
            mid = l + ( r -l )/ /2
            if target > nums[mid]:
                l = mid +1
            else:
                r = mid

        if target != nums[l]:
            return res
        res[0] = l

        # 找到终点位置
        r = len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        res[1] = l - 1

        return res