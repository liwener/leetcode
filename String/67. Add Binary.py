"""
二进制求和：
满二进一，得到一个反向字符，再进行翻转
第0位数单独处理

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) -1, len(b) - 1

        res = ""

        # 模拟十进制求和
        c = 0  # 进位
        while i >= 0 or j >= 0:
            if i >= 0:
                c += int(a[i])
                i -= 1
            if j >= 0:
                c += int(b[j])
                j -= 1
            res += str(c % 2)  # 取余
            c >>= 1  # 除2取整

        # 第0位数单独处理
        if c > 0:
            res += '1'

        return res[::-1]






