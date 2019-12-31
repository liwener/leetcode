"""
方法一：
定义四个边界：上、下、左、右，在边界内进行遍历，
已经使用过的行列，可以将其从图中删去，重新定义边界，
若重新定义后，上下边界交错，表明螺旋矩阵遍历结束，跳出循环，返回答案。

"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        if not matrix:
            return res

        m, n = len(matrix), len(matrix[0])

        # 赋值上下左右边界
        up, down, left, right = 0, m-1, 0, n-1

        while(True):
            # 向右
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up +=1  # 更新边界
            if up >down: break

            # 向下
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -=1
            if right < left: break

            # 向左
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -=1
            if down <up: break

            # 向上
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right: break

        return res
