"""
思路：
先将输入的区间按照第一个元素排序。
将第一个区间放入result中，然后对于后面输入的区间的item.start和result[-1].end比，
如果result[-1].end < item.start，我们就将item加入到result，
否则说明要放入的区间和result[-1]有重叠，那么我们取result[-1].end =max(result[-1].end, item.end)。

时间复杂度：O(nlogn)
除去 sort 的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlgn)

"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for item in intervals:
            if res[-1][-1] < item[0]:
                res.append(item)
            else:
                res[-1][-1] = max(item[-1], res[-1][-1])

        return res

