"""
栈:
   先将字符串依"/"分割出来，然后检查每个分割出来的字符串:
（1）当字符串不为空或"."或".."，则将字符串入栈
（2）当字符串为".."，弹栈（返回上级目录）
   这样栈内的字符就是答案，但是需要进行重新组合，以“/”隔开组合
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == None:
            return
        stack = []

        for s in path.split("/"):
            if s not in ['', '.', '..']:
                stack.append(s)
            elif s == '..' and stack:
                stack.pop()

        return  "/" + "/".join(stack)




