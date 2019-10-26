"""
哈希映射:
在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。
如果它存在，那我们已经找到了对应解，并立即将其返回。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for index, num in enumerate(nums):
            tmp = target - num
            if tmp in hasmap:
                return hasmap[tmp], index
            else:
                hasmap[num] = index
        return None
