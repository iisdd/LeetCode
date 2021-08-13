'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤输入数组的大小。
'''
# 队列,每次求一次最大值,复杂度O(nk), 30.1%
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return []
        from collections import deque
        tmp = deque(nums[:k], maxlen=k)
        res = [max(tmp)]
        for i in range(k, len(nums)):
            tmp.append(nums[i])
            res.append(max(tmp))
        return res

# 维护一个字典,加一个当前最大值,90.8%,字典真好用
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return []
        # 先数前k个
        dct = {}
        for i in range(k):
            dct[nums[i]] = dct.get(nums[i], 0) + 1
        max_num = max(dct.keys())
        res = [max_num]
        # 开始维护字典
        for i in range(k, len(nums)):
            old = nums[i-k]
            new = nums[i]
            dct[old] -= 1
            if dct[old] == 0: del dct[old]
            dct[new] = dct.get(new, 0) + 1
            if new > max_num: max_num = new
            elif max_num not in dct:              # 被删掉了
                max_num = max(dct.keys())
            # 剩下的情况就是最大值保持不变,既没有新来的顶替它,也没有被挤出去
            res.append(max_num)
        return res

# 维护一个单调队列(大的在左),从右边添加新的元素,如果比尾巴的大就挤掉尾巴(pop),双指针(head&tail)遍历
# 如果tail指针指的和队列中左边的最大值相等就把它pop掉
# 76.0%
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0                                                 # 双指针
        if k == 0: return []
        from collections import deque
        tmp = deque([], maxlen=k)
        # 初始化,不pop
        for i in range(k):
            while tmp != deque([]) and nums[r] > tmp[-1]:           # 不为空,跟尾巴比
                tmp.pop()
            tmp.append(nums[r])                                     # 只添加,不弹出
            r += 1
        res = [tmp[0]]
        # 滑动窗开始移动,有新的添加也有老的pop
        for i in range(k, len(nums)):
            while tmp != deque([]) and nums[r] > tmp[-1]:           # 不为空,跟尾巴比
                tmp.pop()
            tmp.append(nums[r])
            r += 1
            if tmp[0] == nums[l]:
                tmp.popleft()
            l += 1
            res.append(tmp[0])
        return res





