'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
# 用时93.8%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 把走过的地方用None标记
        row, column = 0, 0
        turn = 0                            # 0:右,1:下,2:左,3:上
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(m*n):
            res.append(matrix[row][column])
            matrix[row][column] = None
            if turn == 0:
                if column+1 < n and matrix[row][column+1]!=None:        # 往右走
                    column += 1
                else:
                    turn = 1
                    row += 1
                    continue
            elif turn == 1:
                if row+1 < m and matrix[row+1][column]!=None:           # 往下走
                    row += 1
                else:
                    turn = 2
                    column -= 1
                    continue
            elif turn == 2:
                if column-1 >= 0 and matrix[row][column-1]!=None:       # 往左走
                    column -= 1
                else:
                    turn = 3
                    row -= 1
            elif turn == 3:
                if row-1 >= 0 and matrix[row-1][column]!=None:        # 往上走
                    row -= 1
                    print('up')
                else:
                    turn = 0
                    column += 1
        return res
                



















                
        
        
