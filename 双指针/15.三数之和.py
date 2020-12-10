'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
# 用时97.9%,重点是去重复!!!
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()                             # 先对列表排序
        for idx, a in enumerate(nums):          # 遍历列表拿出最小值a
            if a > 0:                           # 最小的都大于0了->跳出循环
                break
            if idx != 0 and a == nums[idx-1]:   # 去除重复
                continue
            l, r = idx+1, n-1                   # 双指针找两数之和
            target = -a
            while l < r:
                summary = nums[l] + nums[r]
                if summary == target:
                    res.append([a,nums[l],nums[r]])
                    # 去重复
                    while l<r and nums[l]==nums[l+1]:
                        l += 1
                    while l<r and nums[r]==nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif summary < target:
                    l += 1
                else:
                    r -= 1
        return res
            
