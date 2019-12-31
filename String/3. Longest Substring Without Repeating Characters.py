"""
滑动窗口：
1、定义一个 map 数据结构存储 (k, v)，其中 key 值为字符，value 值为字符位置 +1，加 1 表示从字符位置后一个才开始不重复
2、定义不重复子串的开始位置为i，结束位置为j
3、随着 j不断遍历向后，会遇到与 [i, j] 区间内字符相同的情况，此时将字符作为 key 值，获取其 value 值，并更新 i。无论是否更新 i，
   都会更新其 map 数据结构和结果 。时间复杂度：O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}  # 用于记录字符的下标
        i, maxlen = 0, 0

        for j in range(len(s)):
            if s[j] in st:
                # 更新左指针，左指针只能一直往右边移动
                i = max(i, st[s[j]])
            maxlen = max(maxlen, j - i + 1)
            # 更新字符下标
            st[s[j]] = j + 1

        return maxlen

