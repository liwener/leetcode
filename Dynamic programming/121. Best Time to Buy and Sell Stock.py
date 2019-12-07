"""
DP思想：
需要找出给定数组中两个数字之间的最大差值(最小谷之后的最大峰)
前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        le = len(prices)
        if le == 0:
            return 0
        # 问题的状态：用两个变量，一个存储当前最大的收益，一个存储当前的最小值。
        min_p, max_p = prices[0], 0

        for i in range(le):
            # 转移方程
            # 比较之前最小值和当前值，更新最小值
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i] - min_p > max_p:
                # 比较之前最大利润和当前利润，更新最大利润
                max_p = prices[i] - min_p

        return max_p

