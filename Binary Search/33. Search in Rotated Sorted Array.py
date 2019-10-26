"""

将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。

1、有序部分用二分法查找。在用首尾两个数来判断目标值是否在这一区域内，这样就可以确定保留哪半边了。

2、无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环。

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)

        if size == 0:
            return -1

        l, r = 0 ,size - 1

        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m

            if nums[m] < nums[r]:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1













