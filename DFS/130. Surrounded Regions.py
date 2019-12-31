"""
思路:从边界出发，先把边界上和 O 连通点找到, 把这些变成 #；
然后遍历整个 board ，把 O 变成 X, 把 # 变成 O。 DFS 或者 BFS都可。

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return

        row, col = len(board), len(board[0])

        # 寻找边界上和0连通的点
        def helper(i, j):
            board[i][j] = "#"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y

                if (1 <= tmp_i < row and 1 <= tmp_j < col):
                    # 未搜索过
                    if board[tmp_i][tmp_j] == "O":
                        helper(tmp_i, tmp_j)

        # 从边缘O开始搜索
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    if board[i][j] == "O":
                        helper(i, j)

        # 遍历整个board，把O变成X，把B变成O
        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # # 变成 O
                if board[i][j] == "#":
                    board[i][j] = "O"






