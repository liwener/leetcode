"""
标准二分查找算法 :二维数组当作一维有序数组考虑，整除和取模把一维坐标转为二维。

初始化左右序号:left = 0 和 right = m x n - 1。

While left <= right :
选取数组中间序号: idx = (left + right) / 2。
整该序号对应于原矩阵中的行 idx // n ; 列 idx % n , 比较 与 target 以确定在哪一部分进行进一步查找。

"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return

        n = len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            idx = l + (r - l) // 2
            tmp = matrix[idx // n][idx % n]
            if target == tmp:
                return True
            elif target > tmp:
                l = idx + 1
            else:
                r = idx - 1

        return False