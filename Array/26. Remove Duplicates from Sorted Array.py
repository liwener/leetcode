"""
双指针法：
数组完成排序后，我们可以放置两个指针 i和 j，其中 i是慢指针，而 j是快指针。只要 nums[i] = nums[j]，我们就增加 j以跳过重复项。
当我们遇到 nums[j] =nums[i] 时，跳过重复项的运行已经结束，因此我们必须把它（nums[j]）的值复制到 nums[i + 1]。
然后递增 i，接着我们将再次重复相同的过程，直到 j到达数组的末尾为止。

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        # 慢指针
        i = 0
        # 快指针
        for j in range(1 ,size):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i+ 1





