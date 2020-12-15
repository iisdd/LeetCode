'''
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
# 用时95.0%,内存5%
class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = {}                    # 用字典记录出现过的数字
        while 1:
            tmp = 0
            while n:
                tmp += (n%10) ** 2
                n //= 10
            if tmp == 1:
                return True
            if tmp in numbers:          # 进入失败的循环了
                return False
            numbers[tmp] = 1
            n = tmp

# 用时95.0%,内存5%...
class Solution:
    def isHappy(self, n: int) -> bool:
        # 试试不增加内存消耗,快慢指针
        def num2sum(num):
            res = 0
            while num:
                res += (num%10) ** 2
                num //= 10
            return res
        fast = n
        slow = n
        while 1:
            fast = num2sum(num2sum(fast))
            slow = num2sum(slow)
            if slow == 1:
                return True
            if slow == fast:                # 失败的循环
                return False















        




