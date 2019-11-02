"""
典型的二分法:找到n，n的平方小于x，n+1的平方大于x，就好
可以用left，right两个指针分别指向两个整数，逼近要求取的值。

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x

        while start <= end:
            # 结果都计算为整数
            mid = start + (end - start) // 2

            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid

            elif x < mid * mid:
                end = mid - 1
            else:
                start = mid + 1