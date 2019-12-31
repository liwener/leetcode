"""
回溯+剪枝
注意：
（1）IP的格式,每位是在0~255之间,
（2）不能出现以0开头的两位以上数字,比如012,08
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, tmplist = [], []
        self.helper(s, tmplist,res)
        return res

    # helper遍历，s为待处理字段，tmp存储所有ip小段
    def helper(self, s, tmp, res):
        if len(tmp) == 4:   # 递归出口，凑够4段
            if len(s) == 0:   # s没有剩余，说明找到一个合法ip，否则返回
                res.append('.'.join(tmp))
            return

        # 遍历取s的头，长度从1到3
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) > 255:
                    return
                elif i >1 and s[0] == '0':
                    return
                # 截断s，并将本次截取内容写入tmp
                self.helper(s[i:], tmp + [s[:i]], res)

