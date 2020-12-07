'''
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1

'''
# 用时97.5%
class Solution:
    def matrixScore(self, A):
        rows, columns = len(A), len(A[0])
        # 先把每一行的头变成1
        for row in A:
            if row[0] == 0:                         # 如果行头是0
                for column in range(columns):       # 整行翻转
                    row[column] = 1-row[column]
        # 再对不完美的列进行翻转
        for c in range(columns):
            column = [A[r][c] for r in range(rows)] # 生成一列的列表
            if sum(column) < rows/2:
                for r in range(rows):
                    A[r][c] = 1-A[r][c]
        res = 0
        for row in A:                               # 开始算和
            sum_row = 0
            for c in range(columns-1, -1, -1):
                sum_row += row[c] * (2**(columns-1-c))
            res += sum_row
        return res





                
