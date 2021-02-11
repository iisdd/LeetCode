'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''
# 用时87.1%
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        # 边界情况,数字不能重复,过大过小都不行
        if n < (1+k)*k/2 or n > (19-k)*k/2 or k > 9:
            return self.res
        self.traceback([], 1, n, k)
        return self.res


    def traceback(self, tmp, start, target, k):          # 为了去重,组合内数字升序
        if k == 1:
            if target >= start and target <= 9:
                self.res.append(tmp+[target])
        else:
            for i in range(start, min(9, target)+1):
                self.traceback(tmp+[i], i+1, target-i, k-1)



