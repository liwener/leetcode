"""
简单的出栈入栈法。
1.逆波兰表达式求解,定义一个栈辅助计算;
2.当遇到运算符"+"、"-"、"*"、"/"时,从栈中pop出两个数字计算,否则将数字入栈;

"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []

        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                b, a = int(stack.pop()), int(stack.pop())
                if i == "+":
                    res = a + b
                if i == "-":
                    res = a - b
                if i == "*":
                    res = a * b
                if i == "/":
                    res = int(a / b)

                stack.append(res)
            else:
                stack.append(i)

        return stack[-1]



