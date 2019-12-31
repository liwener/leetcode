"""
三路快排：（三路快排思想，大于1的放右边，小于1的放左边，等于1的不动）
0，1，2 排序。一次遍历，如果是0，则移动到表头，如果是2，则移动到表尾，不用考虑1。

"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        cur = 0

        while cur <= r:
            # 与l交换值后，因为curr的值已经扫描过了，所以curr要++继续扫描下一位
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
                cur += 1

            # 而与r交换的值，curr未扫描，要停下来扫描一下，所以curr不用++
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1

            else:
                cur += 1


