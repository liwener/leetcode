"""
动态规划：
对于本题而言，采取从底向上遍历法。空间优化为一维，即：
从倒数第二行开始依次遍历，最后dp[0]即是我们想要的结果。

"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 三角形行数
        row = len(triangle)
        # 一位数组进行求解
        dp = [0] * row
        for i in range(row):
            dp[i] = triangle[-1][i]

        # 只需要记录每一层的最小值即可
        for i in range(row - 2, -1, -1):
            for j in range(i+1):
                # 原地修改，这里的dp[j]使用的时候默认的是上一层，赋之后变成当前层
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]

        return dp[0]