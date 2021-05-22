'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

 

示例 1:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: [2,3,0,1,4]
输出: 2
 

提示:

1 <= nums.length <= 1000
0 <= nums[i] <= 105
'''
# 效率71.4%,倒着贪心
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        steps = [0] * n
        i = n-2
        while i >= 0:
            if i+nums[i] >= n-1:    # 一步到终点
                steps[i] = 1
            elif nums[i] == 0:      # 永远出不去
                steps[i] = 1000
            else:
                steps[i] = min(steps[i+1:i+nums[i]+1]) + 1
            i -= 1
        return steps[0]
