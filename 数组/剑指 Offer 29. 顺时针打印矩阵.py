'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length<= 100
'''


# 97.1%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        if row == 0:
            return res
        column = len(matrix[0])
        if column == 0:
            return res
        # 整体流程: 右移h, 下移v-1, 左移h-1, 上移v-2, 右移h-2 ...
        move_length_h = column + 1  # 横向移动距离
        move_length_v = row         # 竖向移动距离
        r, c = 0, -1
        while 1:
            if move_length_v <= 0 or move_length_h <= 0:
                break
            # 右移
            move_length_h -= 1
            for i in range(move_length_h):
                c += 1
                res.append(matrix[r][c])
            if move_length_v <= 0 or move_length_h <= 0:
                break
            # 下移
            move_length_v -= 1
            for i in range(move_length_v):
                r += 1
                res.append(matrix[r][c])
            if move_length_v <= 0 or move_length_h <= 0:
                break
            # 左移
            move_length_h -= 1
            for i in range(move_length_h):
                c -= 1
                res.append(matrix[r][c])
            if move_length_v <= 0 or move_length_h <= 0:
                break
            # 上移
            move_length_v -= 1
            for i in range(move_length_v):
                r -= 1
                res.append(matrix[r][c])
        return res
