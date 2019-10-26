"""
1、将数组排序 ,去重用
2、定义三个指针：i，j，k。遍历i，那么这个问题就可以转化为在i之后的数组中寻找nums[j]+nums[k]=-nums[i]这个问题，
   也就将三数之和问题转变为二数之和。（可以使用双指针）
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size < 3:
            return

        res = []
        # 排序
        nums.sort()

        for i in range(size - 2):
            if nums[i] > 0:
                break
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, size - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                # 找到时
                if threesum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 去重
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif threesum < 0:
                    l += 1
                else:
                    r -= 1
        return res
