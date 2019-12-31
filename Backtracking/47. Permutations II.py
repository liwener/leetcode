"""
回溯法：数组先排序，选择之前先剪枝。

去重:在dfs时要判断i和i-1是否相等和i-1这个值是否被用。
相等和没有被用就跳过这个i的情况，直接去i+1判断。因为没被用之后就可以再用这个i-1，就会出现重复的情况。

"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        # used 标记使用过的数
        used = [False ]* len(nums)
        nums.sort()
        self.helper(nums, 0, used, [], res)
        return res

    def helper(self, array, index, used, path, res):
        if index == len(array):
            res.append(path[:])
            return

        for i in range(len(array)):
            if not used[i]:
                # array[i] 和 array[i-1]的值相等，且array[i-1]没被用过（之后可能会被用就产生重复）
                if i > 0 and array[i] == array[i -1] and not used[i -1]:
                    continue

                used[i] = True
                path.append(array[i])
                self.helper(array, index +1, used, path, res)
                path.pop()
                used[i] = False

