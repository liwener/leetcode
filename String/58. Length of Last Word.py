"""
标签：字符串遍历
主要有两种情况
（1）以字符串"Hello World"为例，从后向前遍历直到遍历到头或者遇到空格为止，即为最后一个单词"World"的长度5
（2）以字符串"Hello World     "为例，需要先将末尾的空格过滤掉，再进行第一种情况的操作，即认为最后一个单词为"World"，长度为5

先从后过滤掉空格找到单词尾部，再从尾部向前遍历，找到单词头部，最后两者相减，即为单词的长度。

时间复杂度：O(n)，n为结尾空格和结尾单词总体长度
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        le, end = 0, len(s) - 1

        while end >= 0 and s[end] == " ":
            end -= 1

        while end >= 0 and s[end] != " ":
            end -= 1
            le += 1

        return le



