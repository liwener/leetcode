"""
利用数组的首行和首列来记录 0 值。从数组下标的 A[1][1] 开始遍历，
两个布尔值记录首行首列是否需要置0

"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_row = is_col = False

        R = len(matrix)
        C = len(matrix[0])

        # 找第一行是否有0
        for j in range(C):
            if matrix[0][j] == 0:
                is_row = True
                break

        # 找第一列是否有0
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
                break

        # 把第一行或者第一列作 标志位
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 置0
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理首行
        if is_row:
            for j in range(C):
                matrix[0][j] = 0

        # 处理首列
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

        return




