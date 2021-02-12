'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''
# 用时89.7%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        n = len(candidates)

        def traceback(tmp, target, start):
            if target == 0:
                self.res.append(tmp)
            else:
                for i in range(start, n):
                    if i > start and candidates[i] == candidates[i-1]:      # 去重,如果在这个位置第一次出现可以放他一马,否则就挖掉
                        continue
                    if candidates[i] > target:
                        break
                    traceback(tmp+[candidates[i]], target-candidates[i], i+1)

        traceback([], target, 0)
        return self.res







