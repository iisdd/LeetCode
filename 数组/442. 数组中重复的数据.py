'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]
'''
# 用时46.9%,原地哈希,把每个数字换到它该去的位置
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):      # 一个位置一个位置的整顿
            if nums[i] == i+1 or nums[i] == 0:
                continue
            while nums[i] != i+1:   # 换到符合条件的就停
                if nums[i] == 0:
                    break
                if nums[i] == nums[nums[i]-1]:  # 换到重复的该位置就置0,然后看下一个
                    res.append(nums[i])
                    nums[i] = 0
                    break
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]    # 交换,注意前后顺序
                print(nums)
        return res
