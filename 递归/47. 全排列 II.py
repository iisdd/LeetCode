'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
# 直接跳过重复字母(与前一个相同),
# 用时99.4%
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        self.res = []
        used = [0 for _ in range(n)]            # 记录是否用过这个数
        self.loop([], nums, used, n)
        return self.res

    def loop(self, tmp, nums, used, n):
        if len(tmp) == n:
            self.res.append(tmp)
        else:
            for i in range(n):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                    # 只有第一个算进去,后面连续重复的都跳过
                    continue
                used[i] = 1
                self.loop(tmp+[nums[i]], nums, used, n)
                used[i] = 0



                
