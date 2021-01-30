'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
# 用时97.7%
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.loop(nums, [], res)
        return res

    def loop(self, li, tmp, res):
        n = len(li)
        if n == 1:
            tmp += li
            res.append(tmp)
        else:
            for i in range(n):              # 条件说了没有重复数字
                self.loop(li[:i]+li[i+1:], tmp+[li[i]], res)













                
