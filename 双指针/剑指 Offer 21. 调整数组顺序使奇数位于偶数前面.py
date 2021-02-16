'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
'''
# 解法1:使用额外空间
# 用时97.7%
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        return odd+even

# 解法2:首尾双指针
# 用时97.7%
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            while l < r and nums[l] % 2:                    # 左指针奇数推进
                l += 1
            while l < r and nums[r] % 2 == 0:               # 右指针偶数推进
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return nums




