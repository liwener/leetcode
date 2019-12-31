class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []

        for c in s:
            # isalnum() 方法检测字符串是否由字母和数字组成。
            if c.isalnum():
                res.append(c.lower())  # lower()将字母全部转化为小写
            else:
                continue

        return res == res[::-1]
