"""
动态规划:
虽然这一算法非常简单，但用于构造杨辉三角的迭代方法可以归类为动态规划,
因为我们需要基于前一行来构造每一行。

"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        # 给数组一个个赋值
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                # 若是左右两边的边界，赋值为1
                if j == 0 or j == i:
                    tmp.append(1)
                # 否则赋值为该位置左上与右上的和
                else:
                    tmp.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(tmp)
        return res

