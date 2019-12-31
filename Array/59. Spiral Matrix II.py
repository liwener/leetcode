"""
生成一个 n×n 空矩阵 mat，随后模拟整个向内环绕的填入过程,
已经使用过的行列，可以将其从图中删去，重新定义边界。

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for _ in range(n)] for _ in range(n)]
        # 赋值上下左右边界
        up, down, left, right = 0, n - 1, 0, n - 1
        c = 1
        while c <= n * n:
            # 从左向右
            for i in range(left, right + 1):
                array[up][i] = c
                c += 1
            up += 1  # 更新边界
            # 从上往下
            for i in range(up, down + 1):
                array[i][right] = c
                c += 1
            right -= 1
            # 从右往左
            for i in range(right, left - 1, -1):
                array[down][i] = c
                c += 1
            down -= 1
            # 从下往上
            for i in range(down, up - 1, -1):
                array[i][left] = c
                c += 1
            left += 1

        return array










