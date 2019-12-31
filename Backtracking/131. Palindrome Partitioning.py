"""
根据递归树编码：在叶子结点是空字符串的时候结算，此时从根结点到叶子结点的路径，就是结果集里的一个结果，
使用深度优先遍历，记录下所有可能的结果。

"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(s, [], res)
        return res

    # s 为待处理字段，tmp 存储所有子回文串
    def helper(self, s, tmp, res):
        if len(s) == 0:
            res.append(tmp)

        for i in range(1, len(s)+1):    # 单个字符也是回文子串
            # 判断子串是否对称
            if s[:i] == s[:i][::-1]:
                self.helper(s[i:], tmp + [s[:i]], res)