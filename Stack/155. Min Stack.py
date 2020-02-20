"""
思想：“以空间换时间”，使用辅助栈。
解题思路：
1、借用一个辅助栈min_stack，用于存获取stack中最小值，
2、入栈时，一个是入栈的元素本身，一个是当前栈元素的最小值。
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 数据栈
        self.stack = []
        # 最小栈
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()