'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''
# 用时98.7%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 用双指针做遍历,碰到val就做交换把指定值丢后边
        n = len(nums)
        i, j = 0, n-1
        res = 0
        while i <= j:
            while j>=0 and nums[j] == val:                  # 换到一个正常的数来
                j -= 1
            if j < i:
                break
            if nums[i] == val:
                nums[i] = nums[j]                           # 不用管后面的是多少
                j -= 1
            res += 1
            i += 1
        return res
        
