'''
给定一个二进制数组， 计算其中最大连续 1 的个数。

示例：

输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
 
提示：

输入的数组只包含 0 和 1 。
输入数组的长度是正整数，且不超过 10,000。
'''
# 用时67.3%
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        tmp = 0
        for i in nums:
            if i == 0:
                res = max(res, tmp)
                tmp = 0
            else:
                tmp += 1
        res = max(res, tmp)
        return res





