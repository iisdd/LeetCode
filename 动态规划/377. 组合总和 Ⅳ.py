'''
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
'''
# 递归超时
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.res = 0
        nums.sort()                         # 先排个序,方便break
        self.traceback(target, nums)
        return self.res

    def traceback(self, target, nums):
        if target == 0:
            self.res += 1
        else:
            for i in nums:
                if i > target:
                    break
                self.traceback(target-i, nums)


# 用时93.3%
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        # 用动态规划,和斐波那契数列一个思路
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(target+1):
            for j in nums:
                if i+j > target:
                    break
                dp[i+j] += dp[i]            # i是i+j的来源之一
        return dp[-1]







