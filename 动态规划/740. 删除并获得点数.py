'''
给你一个整数数组nums，你可以对它进行一些操作。

每次操作中，选择任意一个nums[i]，删除它并获得nums[i]的点数。之后，你必须删除每个等于nums[i] - 1或nums[i] + 1的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''
# 效率47.5%,人类极限了已经
class Solution:
    def deleteAndEarn(self, nums):
        from collections import Counter
        nums.append(0)      # 加个起点
        dct = Counter(nums)
        keys = list(dct.keys())
        up_lim = max(keys)
        dp = [0]            # dp[n]表示到key=n为止能攒到多少点数
        if 1 in keys:
            dp.append(dct[1])
        else:
            dp.append(0)
        idx = 2
        while idx <= up_lim:# 不用判断是否在字典里,直接用get
            best = max(dp[-1], dp[-2]+dct.get(idx, 0)*idx)
            dp.append(best)
            idx += 1
        return dp[-1]