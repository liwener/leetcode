"""
求a的n次方，最朴素的想法一定是把它们乘起来，这样的复杂度是O(n)
利用递归，时间复杂度：O(logn)

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        i = n
        if i < 0: i = -i
        res = 1

        while i != 0:
            if i % 2 != 0:
                res *= x
            x *= x
            i = i // 2

        return res if n > 0 else 1 / res

