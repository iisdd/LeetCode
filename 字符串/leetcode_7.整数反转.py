'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
'''
# 用时35.7%
class Solution:
    def judge(x):
        if x > 2**31-1 or x < -2**31:
            return True
        return False

    def reverse(self, x: int) -> int:
        if x > 2**31-1 or x < -2**31:
            return 0                #  特殊情况溢出
        if x >= 0:
            x = str(x)
            x = x[ : : -1]          #  翻转数字
            x = int(x)
            if x > 2**31-1 or x < -2**31:
                return 0            #  可能本来在范围内，反转后溢出
            else:
                return x
        else:
            x = str(x)
            x = x[1: ]              #  去掉负号
            x = x[ : :-1]
            x = int(x)
            if x > 2**31-1 or x < -2**31:
                return 0
            else:
                return -x
