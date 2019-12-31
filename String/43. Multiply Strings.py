"""
 num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j, i+j+1]
        例: 123 * 45,  123的第1位 2 和45的第0位 4 乘积 08 存放在结果的第[1, 2]位中。
          index:    0 1 2 3 4

                        1 2 3
                    *     4 5
                    ---------
                          1 5
                        1 0
                      0 5
                    ---------
                      0 6 1 5
                        1 2
                      0 8
                    0 4
                    ---------
                    0 5 5 3 5
这样我们就可以单独都对每一位进行相乘计算把结果存入相应的index中

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul = [0] * (len(num1) + len(num2))

        if num1 == "0" or num2 == "0":
            return '0'

        # 数字倒过来，因为计算的时候从最低位迭代
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                tmp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                tmp += mul[i+j+1]   # 先加低位判断是否有新的进位
                mul[i+j] += tmp // 10  # 当前位前一位加上，进位（商作为进位）
                mul[i+j+1] = tmp % 10  # 余数作为当前位

        # 将计算的结果转化成字符串
        res = [str(x) for x in mul]
        res = ''.join(res).lstrip('0')  # lstrip() 用于截掉字符串左边的空格或指定字符

        return res