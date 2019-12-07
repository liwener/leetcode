"""
回溯法+排序剪枝
回溯法+排序剪枝

注意：python、java 语言中“可变对象”在“方法传参”中传递的是引用，如果使用 res.append(path) 的话，在 path 变量里存的就是在叶子结点处 path 变量的引用，而 path变量在最终回溯完成以后是空列表 []，使用 res.append(path) 会得到一堆空列表。
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序去重
        candidates.sort()
        self.helper(candidates, 0, target, [], res)
        return res

    def helper(self, array, index, tar, path, res):
        # 剪枝操作
        if tar < 0:
            return
        if tar == 0:
            res.append(path[:])
            return

        for i in range(index, len(array)):
            path.append(array[i])
            # 因为数字可以无限制重复被选取，因此起始位置还是自己
            self.helper(array, i, tar-array[i], path, res)
            path.pop()