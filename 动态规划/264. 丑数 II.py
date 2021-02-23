'''
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
'''
# 用时23.8%
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 搞3个指针分别代表X2, X3, X5的操作
        p2, p3, p5 = 0, 0, 0
        ugly = [1]
        n -= 1
        while n:
            next_num = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            if next_num == ugly[p2]*2:
                p2 += 1
            elif next_num == ugly[p3]*3:
                p3 += 1
            else:
                p5 += 1
            if ugly[-1] == next_num:            # Ex: 2X3 == 3X2 = 6
                continue
            ugly.append(next_num)
            n -= 1
        return ugly[-1]


# 用时72.1%
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        ugly = [1]
        n -= 1
        while n:
            next_num = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            # 改进点,去重节省运算,同时推进指针
            if next_num == ugly[p2]*2:
                p2 += 1
            if next_num == ugly[p3]*3:
                p3 += 1
            if next_num == ugly[p5]*5:
                p5 += 1
            ugly.append(next_num)
            n -= 1
        return ugly[-1]











