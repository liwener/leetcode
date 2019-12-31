"""
算法原理
(1) 栈先入后出特点恰好与本题括号排序特点一致，即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，；
(2) 建立哈希表 dic 构建左右括号对应关系：key右括号，value左括号；这样查询 2 个括号是否对应只需 O(1)时间复杂度；

建立栈 stack，遍历字符串 s 并按照算法流程一一判断。

"""


class Solution:
    def isValid(self, s: str) -> bool:

        dic = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in dic:
                tmp = stack.pop() if stack else "#"
                if tmp != dic[c]:
                    return False
            else:
                stack.append(c)

        return not stack

