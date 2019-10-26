"""
标签：滑动窗口
1、定义一个 map 数据结构存储 (k, v)，其中 key 值为字符，value 值为字符位置 +1，加 1 表示从字符位置后一个才开始不重复
2、我们定义不重复子串的开始位置为 start，结束位置为 end
3、随着 end 不断遍历向后，会遇到与 [start, end] 区间内字符相同的情况，此时将字符作为 key 值，获取其 value 值，并更新 start，此时 [start, end] 区间内不存在重复字符
无论是否更新 start，都会更新其 map 数据结构和结果 ans。时间复杂度：O(n)

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # map用于记录字符的下标
        st = {}

        # 滑动窗口：双指针
        i, ans = 0, 0
        for j in range(len(s)):
            # 右指针,s[j]为重复字符
            if s[j] in st:
                # 更新左指针,左指针只能一直往右边移动
                i = max(st[s[j]], i)
                # 记录连续长度
            ans = max(ans, j - i + 1)
            # 更新字符下标
            st[s[j]] = j + 1

        return ans
