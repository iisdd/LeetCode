'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 
提示：

1 <= n <= 20
'''
# 用时59.1%,规则驾驶
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        row, column = 0, 0
        turn = 0
        for i in range(1, n**2+1):
            res[row][column] = i
            if turn == 0:
                if column+1 < n and res[row][column+1]==0:        # 往右走
                    column += 1
                else:
                    turn = 1
                    row += 1
                    continue
            elif turn == 1:
                if row+1 < n and res[row+1][column]==0:           # 往下走
                    row += 1
                else:
                    turn = 2
                    column -= 1
                    continue
            elif turn == 2:
                if column-1 >= 0 and res[row][column-1]==0:       # 往左走
                    column -= 1
                else:
                    turn = 3
                    row -= 1
            elif turn == 3:
                if row-1 >= 0 and res[row-1][column]==0:        # 往上走
                    row -= 1
                else:
                    turn = 0
                    column += 1
        return res


# 用时81.7,撞墙转向
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        row, column = 0, -1
        num = 0
        while num <= n**2-1:          # 一次走一轮
            while column+1 < n and res[row][column+1] == 0:     # 右
                num += 1
                column += 1
                res[row][column] = num
            while row+1 < n and res[row+1][column] == 0:        # 下
                num += 1
                row += 1
                res[row][column] = num                
            while column-1 >= 0 and res[row][column-1] == 0:    # 左
                num += 1
                column -= 1
                res[row][column] = num
            while row-1 >= 0 and res[row-1][column] == 0:       # 上
                num += 1
                row -= 1
                res[row][column] = num
        return res








        
    
