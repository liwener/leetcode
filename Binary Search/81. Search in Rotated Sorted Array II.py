"""
二分搜索：必须有序，处理区间边界
1、先判断那边区间有序
2、再判断在那边二分搜索
3、注意处理重复数字
————————————————————————————————————————
二分法分类讨论：一共两种可能性，这两种情况各自又有两种可能性

1、左半边是有序的
(1) target落在左半边
2) otherwise

2、右半边是有序的
(1) target落在右半边
(2) otherwise

"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums ) -1

        while l <= r:
            # 处理重复数字，例子：[3，1，1]
            while l < r and nums[l ]= =nums[ l +1]:
                l += 1
            while l < r and nums[r ]= =nums[ r -1]:
                r - =1

            mid = l + ( r -l )/ /2
            if targe t== nums[mid]:
                return True
            else:
                # 在右区间有序
                if nums[mid] < nums[r]:
                    if nums[mid] < target and target < =nums[r]:
                        l = mid +1
                    else:
                        r = mid - 1
                # 左区间有序
                else:
                    if nums[l] <= target and target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1

        return False