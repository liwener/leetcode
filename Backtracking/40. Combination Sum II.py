"""
回溯法+排序剪枝：
(1) 每一层往下搜索的时候，只能从这个数的后面开始进行搜索（而不是从这个数的位置开始进行搜索）。
(2) 还有一点可能引起重复的情况，就是同一层中，如果后面的数和前面的数相同，就会引发重复，这个时候直接continue。
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序便于剪枝去重
        candidates.sort()
        self.helper(candidates, 0, target, [], res)
        return res

    def helper(self, array, index, tar, path, res):
        # 剪枝
        if tar < 0:
            return
        if tar == 0:
            res.append(path[:])
            return
        for i in range(index, len(array)):
            #  "剪枝" 检测到重复分支的条件：
            # （1）不是这一层的第一个分支
            # （2）当前选出来的数和前一个分支相等
            if i > index and array[i] == array[i - 1]:
                continue
            path.append(array[i])
            self.helper(array, i + 1, tar - array[i], path, res)
            path.pop()