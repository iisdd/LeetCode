'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
'''
# 先用Counters检验一下结果,用时45.9%,有排序O(nlogn)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        res = []
        dct = Counter(nums)
        n = len(nums)
        for i in range(1, n+1):
            if i not in dct:
                res.append(i)
        return res


# 原地哈希,把数字n放在位置n-1上,O(n)用时81.4%
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = [0] + nums                   # 加个头让下标和数值对应,方便操作
        for idx, val in enumerate(nums):
            last_val = val
            while idx != val:
                nums[idx] = last_val        # 上一个val归位
                idx = val                   # 指向下一个元素
                last_val = val              # 保存当前value
                val = nums[idx]             # 更新下下个元素指针

        res = []
        for idx, val in enumerate(nums):
            if idx != val:
                res.append(idx)
        return res














