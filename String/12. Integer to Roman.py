"""
把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中，
并且按照阿拉伯数字的大小降序排列，这是贪心选择思想，
每一步都使用当前较大的罗马数字作为加法因子，最后得到罗马数字表示就是长度最少的。
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        index = 0
        res = ''
        while index < 13:
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1

        return res
