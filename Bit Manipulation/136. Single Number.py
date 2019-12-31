"""
位运算：

交换律：a ^ b ^ c <=> a ^ c ^ b

任何数与0异或为任何数 0 ^ n => n

相同的数异或为0: n ^ n => 0

"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = res ^ num

        return res

