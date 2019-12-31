"""
按行排序: 从左向右迭代字符串,将每个字符添加到合适的行,使用当前行和当前方向这两个变量对合适的行进行跟踪。
         只有当我们向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # 使用 min(numRows,len(s))个列表来表示Z字形图案中的非空行。
        rows = ['']*min(numRows, len(s))
        curRow = 0
        goingdown = -1
        # 按行排序，从左向右迭代字符串
        for c in s:
            # 变换方向
            if curRow == 0 or curRow == numRows-1:
                goingdown = goingdown*(-1)

            rows[curRow] += c
            curRow += goingdown

        res = ''
        for row in rows:
            res += row

        return res