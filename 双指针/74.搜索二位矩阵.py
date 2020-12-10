'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
'''
# 用时87.4%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 进行两次二分查找
        li = matrix
        num = target
        # 特殊情况检查
        m = len(li)
        if m == 0:
            return False
        n = len(li[0])
        if n == 0:
            return False
        # 双指针找行
        l, r = 0, m-1
        row = -1
        while l < r:
            mid = (l+r) // 2
            if mid == m-1 or (li[mid][0]<=num and li[mid+1][0]>num):        # mid为要找的行
                row = mid
                break
            elif li[mid][0] < num:
                l = mid+1
            else:
                r = mid-1
        if row == -1:                                                       # 因为l == r跳出循环的
            row = l
        print('所在行: ', row)
        # 再来一遍双指针找列
        l, r = 0, n-1
        column = -1
        tmp = li[row]
        if tmp[-1] < num:                                                   # 一行的最大值都没num大
            return False    
        while l <= r:
            mid = (l+r) // 2
            if tmp[mid] == num:
                column = mid
                print('所在列: ', column)
                return True
            elif tmp[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
