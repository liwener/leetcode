"""
 动态规划：
因为我们只需要返回第k行的结果，所以相比于前一题，
我们不需要记录整个三角形的数，只需要对一行数组不断循环操作即可。

"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0]* (rowIndex+1)

        for i in range (rowIndex+1):
            for j in range(i, -1, -1):
                # 倒序遍历，就可以直接使用上一层的结果
                if j == 0 or j ==i:
                    res[j] = 1
                else:
                    res[j] += res[j-1]

        return res