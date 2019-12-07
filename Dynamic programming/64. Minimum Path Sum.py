"""
动态规划：dp[i][j]代表从(0,0)走到(i,j)的最小路径和
特殊处理：
dp[0][i]来自第一行的累加
dp[i][0]来自第一列的累加
状态转化方程:
dp[i][j] = min(dp[i-1][j],dp[i][j-1])+c[i][j](来自当前位置的走法无非向下或向右，选两者中代价最小的)

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m == 0:
            return

        # 处理第一行
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        # 处理第一列
        for j in range(1, m):
            grid[j][0] += grid[j - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                # 状态转化方程
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]