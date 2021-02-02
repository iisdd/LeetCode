'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
# 用时93.0%
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        if k > n:
            return self.res
        self.traceback(n, k, [0])
        return self.res
        
    def traceback(self, n, k, tmp):
        if k == 0:
            self.res.append(tmp[1:])
        else:
            for i in range(tmp[-1]+1, n-k+2):
                self.traceback(n, k-1, tmp+[i])
                
