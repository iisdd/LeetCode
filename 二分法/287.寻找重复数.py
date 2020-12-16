'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n^2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
'''
# 时间换空间,效率肯定不会太高,47.5%
class Solution:
    def findDuplicate(self, nums):
        # 按照要求,不能排序,不能用集合存出现的元素
        # 思路:二分法,数两个区间内包含的元素数量
        # 重复数在的那个区间肯定要多些
        # 注意边界条件!!!
        left = 1
        n = len(nums) - 1
        right = n
        curSum = n+1                        # 当前的总区间数
        while left < right:
            mid = (left+right) // 2
            total = 0                       # 左边区间计数
            # print(left, right, mid, curSum)
            for i in nums:
                
                if i <= mid and i >= left:
                    total += 1
            if total > curSum/2:                # total本来就是个大区间(偶数相同,奇数多一个)
                right = mid
                curSum = total
            else:
                left = mid+1
                curSum -= total
        return left

c = Solution
print(c.findDuplicate(c, [1,4,4,2,4]))








            
            

