"""
“回溯 + 剪枝” 。
以下几点考虑：
1、我们知道所求排列一定在叶子结点处得到。事实上，进入每一个分支的时候，我们都可以通过递归的层，直接计算这一分支可以得到的叶子结点的个数。

这是因为：进入一个分支的时候，我们可以根据已经选定的数的个数，进而确定还未选定的数的个数，然后计算阶乘，就知道这一个分支的叶子结点有多少个。

2、如果 k大于这一个分支将要产生的叶子结点数，直接跳过这个分支，即“剪枝”即可。

3、如果 k小于等于这一个分支将要产生的叶子结点数，那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解。

4、计算阶乘的时候，你可以使用循环计算，特别注意：0!=1，它表示了没有数可选的时候，即表示到达叶子结点了，排列数只剩下 1 个。

"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        used = [False] * n
        nums = [i + 1 for i in range(n)]
        self.helper(nums, used, n, k, 0, res)
        return ''.join(res)

    def permutation(self, n):
        # 这种编码方式包括了 0 的阶乘是 1 这种情况
        res = 1
        while n:
            res *= n
            n -= 1
        return res

    def helper(self, nums, used, n, k, depth, res):
        # 在叶子结点处结算
        if depth == n:
            return res

        # 后面的数全排列的个数
        ps = self.permutation(n - 1 - depth)

        for i in range(n):
            # 如果数用过，就不再考虑
            if used[i]:
                continue
            # 后面的数全排列的个数小于k时剪枝
            if ps < k:
                k -= ps
                continue

            # 直接走到叶子结点，状态不用恢复
            used[i] = True
            res.append(str(nums[i]))
            return self.helper(nums, used, n, k, depth + 1, res)


