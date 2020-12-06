'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
# 用时98%
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0 : return []
        res = [[1]]
        for i in range(2, numRows+1):
            tmp = [0] * i            # 初始化
            tmp[0] = res[-1][0]      # 定义头尾
            tmp[-1] = res[-1][-1]
            for j in range(1, i-1):
                tmp[j] = res[-1][j-1] + res[-1][j]
            res.append(tmp)
        return res
