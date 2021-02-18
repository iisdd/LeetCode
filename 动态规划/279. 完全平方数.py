'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

 

示例 1：

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
 
提示：

1 <= n <= 104
'''
# 超时了,感觉很多数字没必要算出来,算那些能得出n的就好
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1 for _ in range(n+1)]      # 每个数都取很大,后面取min
        dp[0] = 0                           # 起点
        for i in range(n):                  # n加1 = n+1,所以遍历到n就好
            for j in range(1, int((n-i)**0.5)+1):
                dp[i+j**2] = min(dp[i+j**2], dp[i]+1)
        return dp[-1]



# 用时18.7%,不能算去处,要算来处...
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1, n + 1):
            val = i         # 最大不过如此
            j = 1
            while i - j * j >= 0:
                val = min(val, dp[i - j*j] + 1)
                j += 1
            dp[i] = val
        return dp[n]



















