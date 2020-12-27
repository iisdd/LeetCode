'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''
# 用时5%,顶级脑瘫
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 用字典存sum {i:sum(nums[0:i])}
        temp_sum = 0
        cur_sum = {}
        for idx, val in enumerate(nums):
            temp_sum += val
            cur_sum[temp_sum] = cur_sum.get(temp_sum, [])+[idx]
        keys = cur_sum.keys()
        print(keys)
        res = 0
        for key in keys:
            if key-k==0:
                res += len(cur_sum[key])
            if key-k in cur_sum:
                for i in cur_sum[key]:
                    for j in cur_sum[key-k]:
                        if i > j:
                            res += 1
        return res


# 前缀和,还是O(n^2),超时
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_sum = [0]*(n+1)
        for i in range(1, n+1):         # cur_sum[i]代表sum(nums[:i])
            cur_sum[i] = nums[i-1] + cur_sum[i-1]
        res = 0
        for i in range(1, n+1):         # i=1时就数过了满足条件的前缀和了
            for j in range(i, n+1):     # [i-1:j]的和
                if cur_sum[j] - cur_sum[i-1] == k:
                    res += 1
        return res


# 我悟了...不能先一次性全拿字典统计出来,要动态的统计
# 用时66.0%
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        dct = {0:1}                             # 0个元素的和出现过一次了
        res = 0
        for i in nums:
            cur_sum += i
            res += dct.get(cur_sum-k, 0)        # 这句放前面,防止k=0的情况
            dct[cur_sum] = dct.get(cur_sum, 0) + 1
        return res
        

        
