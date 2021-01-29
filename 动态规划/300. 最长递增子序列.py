'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 
进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''
# 方法一: 动态规划 O(n^2),更新长度为i的nums的最长递增子序列
# 用时19.2%
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        

# 方法二: 动态规划+二分查找 O(nlogn),外面找更大的,里面更新小的
# 84.7%
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        res = 0
        for num in nums:
            l, r = 0, res
            while l < r:            # 如果比尾巴还大就加在尾巴,否则更新中间的数
                mid = (l+r)//2
                if dp[mid] < num:
                    l = mid+1
                else:
                    r = mid
            dp[l] = num
            if r == res:            # 添加在尾巴处
                res += 1            # 长度加1
        return res
            
        
























        
