"""
加一的所有可能情况只有两种：
1、除 9 之外的数字加1；
2、数字 9。

所以只需要判断有没有进位并模拟出它的进位方式。
从最后一位出发，确定这个 1 应该加在哪个位置。
如果找不到位置，说明溢出了当前数组。新建一个 长度+1 的数组即可。

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) -1

        for i in range(l, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        digits.append(0)
        digits[0] = 1

        return digits