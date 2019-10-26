"""
动态规划:
基本的表达式: area = min(height[i], height[j]) * (j - i) 使用两个指针，值小的指针向内移动，这样就减小了搜索空间。
双指针法:扩大面积
因为面积取决于指针的距离与值小的值乘积。向内移动，距离一定减小，值小的指针向内移动遍历,才可能增加高度以扩大面积。
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height)-1

        while i < j:
            res = max(min(height[i], height[j])* (j-i),res)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
