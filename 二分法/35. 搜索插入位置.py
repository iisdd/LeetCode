'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
'''
# 用时83.0%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        # 跳出循环有三种可能:1.相等->l, 2.大于->l, 3.小于->l+1
        return l if nums[l]>=target else l+1



        
