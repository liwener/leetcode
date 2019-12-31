"""
这道题关键在于：如何找到可以唯一标识具有相同字母并且个数也一样的键。
我们将每个字符串按照字母顺序排序，这样的话就可以把 eat，tea，ate 都映射到 aet。其他的类似。
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            # sorted 返回一个有序的副本
            key = "".join(sorted(s))
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)

        res = list(dic.values())
        return res
