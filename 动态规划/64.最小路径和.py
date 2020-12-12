'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，
使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''
# 改进点:直接修改原矩阵没有新的内存消耗
# 转移矩阵: dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
# 用时99.6%
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划算出从起点到每个点的最短距离
        m = len(grid)
        n = len(grid[0])
        # 先定义两条边的dp值
        for j in range(1, n):                                 # 上边
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1, m):                                 # 左边
            grid[i][0] = grid[i-1][0] + grid[i][0]
        # 计算中间的dp值
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
        return grid[-1][-1]
                
        
