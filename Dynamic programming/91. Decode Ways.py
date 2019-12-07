"""
约束版的f(n) = f(n-1) + f(n-2)
两个约束条件：
（1）0不能单独解码
（2）两位数必须在1与26之间

运用标准的动态规划即可：
建立动态规划数组dp，dp[i]用于记录字符串至第i-1位的解码方法的总数
分成两种情况:
当数字A[i]在区间[1,26]中时, 说明A[i]单独解码, d[i+1] += d[i]
当数字A[i,i+1]在区间[1,26]中. 说明A[i,i+1]单独解码.d[i+1] += d[i-1]

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        le = len(s)
        #边界条件
        if le== 0 or s[0] == "0":
            return 0
        # dp[i+1]用于记录字符串至第i位的解码方法的总数。（需要标记三位，中间位用i标记）
        dp = [0]*(le+1)
        dp[0] = 1

        for i in range(le):
            # 当前组合数量包括前一位数字前的组合总数
            if s[i] == "0":
                dp[i+1] = 0
            else:
                dp[i+1] += dp[i]

            # 当前组合数量包括前两位数字前的组合总数
            if i > 0 and (s[i-1] =="1" or (s[i-1]=="2" and s[i] <= "6")):
                dp[i+1] += dp[i-1]

        return dp[-1]


