"""
组合问题

"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(n, k, 1, [], res)
        return res

    def helper(self, n, k, index, path, res):
        if len(path) == k:
            res.append(path[:])
            return

        for i in range(index, n+1): 
            path.append(i)
            # 因为已经把 i 加入到 path 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self.helper(n, k, i+1, path, res)
            path.pop()