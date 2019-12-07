"""
 回溯法，三个要素：
 1、选择，此题的解就是合法的括号组合，选择就是要么放入左括号，要么放入右括号
 2、条件，放入左括号还是右括号，是有条件约束的，不是随便放到，如果我们还剩位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。
 3、结束条件就是，左右括号都放完了。

"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+ '(', left+1, right)
            if right < left:
                backtrack(S+ ')', left, right+1)

        backtrack('', 0, 0)
        return ans