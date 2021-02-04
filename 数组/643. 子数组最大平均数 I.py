'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例：

输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 
提示：

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
'''
# 用时95.1%
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = sum(nums[:k])
        res = cur_sum
        for i in range(k, n):
            cur_sum += nums[i]-nums[i-k]
            res = max(res, cur_sum)
        return res/k
        












        
