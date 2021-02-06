'''
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]
 
提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
# 用时82.7%
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 其实就是重新排列列表顺序,让出来的数字比刚才大一点点,找不到就重返最小值
        n = len(nums)
        head, tail = self.helper(nums)
        if head < 0:
            nums.sort()                         # 升序排列
            return
        # 交换头尾
        nums[head], nums[tail] = nums[tail], nums[head]
        # 冒泡head后半段
        for t in range(n-1-head):
            for i in range(head+1, n-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

    def helper(self, nums):                     # 辅助函数,找交换的头尾
        n = len(nums)
        for i in range(n-2, -1, -1):            # 头
            for j in range(n-1, i, -1):         # 尾
                if nums[i] < nums[j]:
                    return i, j
        return -1, -1                           # 没找到提升字典序的方法










        
