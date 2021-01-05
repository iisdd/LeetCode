'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''
# 用时78.9%
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 先补零
        n1 = len(num1)
        n2 = len(num2)
        if n1 > n2:
            num2 = '0'*(n1-n2) + num2
        else:
            num1 = '0'*(n2-n1) + num1
        # 维护cur和carry
        res = ''
        carry = 0
        for i in range(max(n1, n2)-1, -1, -1):
            cur = int(num1[i])+int(num2[i])+carry
            res = str(cur%10) + res
            carry = cur//10
        return '1'+res if carry else res  
