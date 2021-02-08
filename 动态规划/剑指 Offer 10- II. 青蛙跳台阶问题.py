'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100
'''
# 递归超时
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return max(1, n)
        else:
            return self.numWays(n-1) + self.numWays(n-2)

# 动态规划,用时98.2%
class Solution:
    def numWays(self, n: int) -> int:
        if n <= 2:
            return max(n, 1)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1] % 1000000007






