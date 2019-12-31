"""
这个形式从逻辑上讲，似乎和“斐波那契数列”有点相似，都是依赖于之前的结果，得到之后的结果，所以，和“斐波那契数列”的做法一样，可以用递归。
使用递归：每次先获取上次的报数，然后依次进行统计，递归退出条件为n=1

"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)

        i = 0
        count = 1
        res = ''

        # 获取上次的报数
        temp = self.countAndSay(n - 1)

        while i < len(temp):
            while i < len(temp) - 1 and temp[i] == temp[i + 1]:
                count += 1
                i += 1
            res += str(count) + str(temp[i])
            # 重新初始化开始统计
            count = 1
            i += 1

        return res