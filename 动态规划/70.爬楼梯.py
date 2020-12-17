'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''
# 用时93.8%
class Solution:
    def climbStairs(self, n: int) -> int:
        #  斐波那契数列,动态规划
        from collections import deque
        # 维护一个长度为2的双向队列
        res = deque([1, 1], maxlen=2)          # 爬1阶有1种方法
        for i in range(n):
            res.append(sum(res))
        return res[0]
        

