"""
标签：动态规划
本问题可以分成多个子问题，爬第n阶楼梯的方法数量，等于 2 部分之和
1、爬上 n-1阶楼梯的方法数量。因为再爬1阶就能到第n阶
2、爬上 n-2阶楼梯的方法数量，因为再爬2阶就能到第n阶
所以我们得到公式 dp[n] = dp[n-1] + dp[n-2]
同时需要初始化 dp[0]=1和 dp[1]=1

时间复杂度：O(n)

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]