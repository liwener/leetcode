"""
用哈希映射来跟踪所有已经遇到的值。
遍历数独:
检查看到每个单元格值是否已经在当前的行 / 列 / 子数独中出现过：
如果出现重复，返回 false。
如果没有，则保留此值以进行进一步跟踪。
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 记录某行，某位数字是否已经被摆放
        row = [set() for i in range(9)]
        # 记录某列，某位数字是否已经被摆放
        col = [set() for i in range(9)]
        # 记录某 3x3 宫格内，某位数字是否已经被摆放
        block = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                pos = (i // 3) * 3 + j // 3

                if item != '.':
                    if item not in row[i] and item not in col[j] and item not in block[pos]:
                        row[i].add(item)
                        col[j].add(item)
                        block[pos].add(item)
                    else:
                        return False

        return True
