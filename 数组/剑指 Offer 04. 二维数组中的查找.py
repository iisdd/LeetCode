'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。

给定target=20，返回false。

限制：

0 <= n <= 1000

0 <= m <= 1000
'''

# 递归试过了,不行...
# 99.2% 复杂度O(n),非常牛
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 根据题目的条件可以推出对于每个位置上的数字,它左边一行都比它小,下面一列都比它大
        # 可以根据这个来淘汰
        # Ex:target比当前数大 -> 下移一格,淘汰掉左边一行. target比当前小 -> 左移一格,淘汰掉下面一列
        # 为了涵盖所有数字,起点选在右上角
        row = len(matrix)
        if row == 0:
            return False
        column = len(matrix[0])
        if column == 0:
            return False

        r, c = 0, column-1
        while r < row and c >= 0:
            cur = matrix[r][c]
            if cur == target:
                return True
            elif cur < target:          # 下移
                r += 1
            else:                       # 左移
                c -= 1
        return False
