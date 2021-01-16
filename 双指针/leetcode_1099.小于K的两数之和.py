'''
给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，
使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和。

如不存在这样的两个元素，请返回 -1。

 

示例 1：

输入：A = [34,23,1,24,75,33,54,8], K = 60
输出：58
解释：
34 和 24 相加得到 58，58 小于 60，满足题意。
示例 2：

输入：A = [10,20,30], K = 15
输出：-1
解释：
我们无法找到和小于 15 的两个元素。
 

提示：

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 效率双百
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # 思路：排序之后双指针往中间逼
        A.sort()
        n = len(A)
        if n == 1 or A[0] + A[1] >= K:
            return -1
        i = 0
        j = n-1
        res = 0
        while i < j:
            tmp = A[i] + A[j]
            if tmp < K:
                res = max(res , tmp)
                i += 1
            elif tmp >= K:
                j -= 1
        return res











        
