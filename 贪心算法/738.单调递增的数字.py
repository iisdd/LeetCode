'''
给定一个非负整数 N，找出小于或等于 N 的最大的整数，
同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。
'''
# 用时67.7%
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 贪心算法,在保证能递增的前提下,找出每一位上的最大值
        # Ex: 1111 < 1352, res += '1'
        #       333 < 352, res += '3'
        #         55 > 52, res += '49'
        l = len(str(N))                             # 位数
        num = str(N)                                # 数字的字符串形式
        res = ''
        for i in range(l):                          # i表示从高到低第几位
            if int(num[i]*(l-i)) <= int(num[i:]):   # 正好极限递增
                res += num[i]
            else:                                   # 这一位要减一的情况
                res += str(int(num[i])-1)
                res += '9' * (l-1-i)                # 减一补满9
                break
        return int(res)

                    
                
            
