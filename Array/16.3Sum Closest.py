"""
先排序, 然后遍历, 然后内部使用双指针, 时间复杂度应该是O(n²)
利用 abs 函数做一个返回值的更改。
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size < 3:
            return

        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for i in range(size - 2):
            l, r = i + 1, size - 1

            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if abs(target - threesum) < abs(target - res):
                    res = threesum

                if threesum < target:
                    l += 1
                elif threesum > target:
                    r -= 1
                else:
                    # 如果已经等于target的话, 是最接近的
                    return target

        return res
