'''
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 
nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数
（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2 
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
进阶：是否能在 O(n2) 的时间复杂度内解决？
'''
# 用时93.6%
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)                       
        # 遍历首元素,双指针夹剩下的
        for i in range(n-2):
            l = i+1
            r = n-1  
            while l < r:
                if nums[l]+nums[r] >= target-nums[i]:
                    r -= 1
                else:
                    res += r-l
                    l += 1
        return res





        
