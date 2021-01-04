'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''
# 用时72.1%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 内置函数解法
        return bin(int(a,2)+int(b,2))[2:]

# 用时52.3%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 字符串解法,先补满0,维护当前位的数cur与进位carry
        na = len(a)
        nb = len(b)
        n = max(na, nb)
        if na >= nb:
            b = '0'*(na-nb) + b
        else:
            a = '0'*(nb-na) + a
        res = ''
        carry = 0
        for i in range(n-1, -1, -1):
            cur = int(a[i]) + int(b[i]) + carry
            res = str(cur%2) + res
            carry = cur // 2
        return '1'+res if carry else res
            
        
        
