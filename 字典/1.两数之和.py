'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
# 用时86%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for idx, val in enumerate(nums):        # 元素作key，位置作value
            dct[val] = idx
        for i, num in enumerate(nums):
            j = dct.get(target - num)           # get如果没有找到会返回None
            if j and  j!= i :                   # j肯定不会为0(j > i)
                return[i , j]
