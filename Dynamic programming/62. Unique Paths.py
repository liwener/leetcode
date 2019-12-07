"""
思路：

(1)、考虑位置X,Y。到达该位置一共有2条线路，从上面的格子过来或从左边的格子过来
(2)、所以 f(m,n) = f(m-1,n) + f(m,n-1)
(3)、特殊情况，边缘位置，当x等于1时，只能从上面过来,当y等于 1时，只能从左边过来。

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # 考虑特殊情况
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # f(m,n) = f(m-1,n) + f(m,n-1)
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
