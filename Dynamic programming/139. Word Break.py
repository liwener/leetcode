"""
状态转移方程：dp[i] = s[j:i] in wordDict and dp[j]。

注意 ：
1、需要长度为 0的状态，且定义为 True，因为如果字符串本身就在 wordDict 中，就不必看 dp 了，可以直接判断为 True，因此 dp[0] = True；
2、注意边界条件：后数组的起始索引，表示了前数组的长度；
3、一旦得到 dp[i] = True 就可以退出循环了，j 就无须遍历下去。

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        # 状态定义：dp[i]表示s中以i-1结尾的字符串是否可被 wordDict 拆分
        dp = [False for _ in range(size+1)]
        dp[0] = True

        # 使用r表示右边界，使用l 表示左边界
        for r in range(1, size+1):
            for l in range(r):
                # dp[l] 写在前面会更快一点，否则还要去切片，然后再判重
                if dp[l] and s[l:r] in wordDict:
                    dp[r] = True
                    # 这个 break 很重要，一旦得到 dp[r] = True ，循环不必再继续
                    break

        return dp[-1]