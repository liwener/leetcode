"""
上一题的基础上加上判断：
（1）如果当前网格的值为0，和上一题一样
（2）如果当前网格的值为1，到此网格的路径数归0
（3）注意边界情况的处理

"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 0 or obstacleGrid[0][0] == 1:
            return 0

        # 首位置
        obstacleGrid[0][0] = 1
        # 第一行
        for i in range(1, n):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] if obstacleGrid[0][i] == 0 else 0
        # 第一列
        for j in range(1, m):
            obstacleGrid[j][0] = obstacleGrid[j - 1][0] if obstacleGrid[j][0] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0

        return obstacleGrid[-1][-1]

