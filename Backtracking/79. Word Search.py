"""
使用深度优先搜索（DFS）和回溯的思想实现。
（1）外层：遍历
         首先遍历 board 的所有元素，先找到和 word 第一个字母相同的元素，然后进入递归流程。假设这个元素的坐标为 (i, j)，进入递归流程前，先记得把该元素打上使用过的标记：mark[i][j] = 1
（2）内层：递归
        从 (i, j) 出发，朝它的上下左右试探，看它周边的这四个元素是否能匹配 word 的下一个字母。如果匹配到了，带着该元素继续进入下一个递归。如果都匹配不到，返回 False
        当 word 的所有字母都完成匹配后，整个流程返回 True
"""


class Solution:
    # 定义上下左右四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word) -> bool:
        m = len(board)
        if m == 0:
            return False

        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]
        # 外层遍历：对每一个格子都从头开始搜索
        for i in range(m):
            for j in range(n):
                # 内层递归：只要有一个返回true，那么就表示可以找到对应的字符串
                if self.helper(board, word, mark, i, j, 0):
                    return True
        return False

    def helper(self, board, word, mark, i, j, index):
        if index == len(word) - 1:
            return word[index] == board[i][j]

        # 中间匹配了，再继续搜索
        if board[i][j] == word[index]:
            # 将该元素标记为已使用
            mark[i][j] = 1

            for direct in self.directs:
                x = i + direct[0]
                y = j + direct[1]

                if 0 <= x < len(board) and 0 <= y < len(board[0]) and mark[x][y] == 0:
                    if self.helper(board, word, mark, x, y, index + 1):
                        return True

            # 回溯
            mark[i][j] = 0

        return False