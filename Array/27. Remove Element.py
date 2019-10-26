"""
双指针法:
当 nums[j]与给定的值相等时，递增 j以跳过该元素。只要 nums[j]!=val
我们就复制 nums[j] 到 nums[i] 并同时递增两个索引。重复这一过程，直到 j 到达数组的末尾，该数组的新长度为 i

"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        # i记录不等于val的个数
        i = 0
        for j in range(size):
            if val != nums[j]:
                nums[i] = nums[j]
                i += 1

        return i



