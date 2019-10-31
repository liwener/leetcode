"""
这题主要考两点，
1）负数的表示方法（最高位为1，减去其余位）
2）使用左移形成2的指数倍，加快运算
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        # 用计算是否符号相异
        negative = 1 if (dividend > 0) != (divisor > 0) else 0

        # 取绝对值来运算
        t = abs(dividend)
        d = abs(divisor)
        res = 0

        for i in range(32, -1, -1):
            # 找出足够大的数2^n*divisor
            if t >> i >= d:
                # 将结果加上2^n
                res += 1 << i
                # 将被除数减去2^n*divisor
                t -= d << i

        return -res if negative else res