'''
整数可以被看作是其因子的乘积。

例如：

8 = 2 x 2 x 2;
  = 2 x 4.
请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。

注意：

你可以假定 n 为永远为正数。
因子必须大于 1 并且小于 n。
示例 1：

输入: 1
输出: []
示例 2：

输入: 37
输出: []
示例 3：

输入: 12
输出:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
示例 4:

输入: 32
输出:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''
# 用时96.4%
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.res = []
        self.traceback(n, [], 2)                    # 因数>=2
        return self.res
    def traceback(self, n, tmp, start):             # start为最小因数,为了去重,因数必须从小到大排列
        if n == 1:
            return
        for i in range(start, int(n**0.5)+1):
            if n / i == n // i:
                self.res.append(tmp+[i]+[n//i])
                self.traceback(n//i, tmp+[i], i)    # 下一个因数不能比i小



























