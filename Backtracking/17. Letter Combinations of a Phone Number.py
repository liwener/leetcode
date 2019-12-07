"""
回溯:通过穷举所有可能情况来找到所有解
问题转化成了从根节点到空节点一共有多少条路径

"""



class Solution:
    def __init__(self):
        # 构造字典
        self.letterMap = [
            '',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]

    def findCombination(self, digits, index, s, res):
        # 深搜触底，回溯
        if index == len(digits):
            res.append(s)
            return

        char = digits[index]
        letters = self.letterMap[ord(char) - ord('0')]
        # 遍历某个数字代表的所有字典
        for letter in letters:
            # 从下一位开始，到最后的组合情况
            self.findCombination(digits, index + 1, s + letter, res)

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result

        self.findCombination(digits, 0, "", result)
        return result


