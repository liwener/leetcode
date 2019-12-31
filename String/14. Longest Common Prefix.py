"""
纵向比较数组每个单词的同一位置， 直到出现不同字符串，或者长度不一致时，返回已经匹配的长度。

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        # 第一个字符串当模板串
        tmp = strs[0]
        # 遍历后面的字符串，依次与模板串逐位进行比较
        for i in range(len(tmp)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != tmp[i]:
                    return strs[0][:i]

        return strs[0]




