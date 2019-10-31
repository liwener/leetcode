"""
思路，二分查找，如果找到值，返回值的位置，
如果循环结束也没有找到，根据 target 的值和  nums[mid] 的比较来判断值应该插入在哪里，不是在 mid 前面 就是在 mid 后面。

"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l