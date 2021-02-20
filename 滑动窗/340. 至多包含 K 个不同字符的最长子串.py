'''
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。
'''
# 用时95.0%
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dct = {}                        # 用来记录现有元素成分
        res = 0
        n = len(s)
        l, r = 0, 0
        while r < n:
            while k >= 0 and r < n:     # 右指针推进
                if dct.get(s[r], 0):
                    dct[s[r]] += 1
                else:
                    k -= 1
                    dct[s[r]] = dct.get(s[r], 0) + 1
                    res = max(res, r-l) # k减到-1时更新res
                r += 1
            while k == -1:              # 左指针推进
                dct[s[l]] -= 1
                if dct[s[l]] == 0:
                    k += 1
                l += 1
        res = max(res, r-l)             # r = n走到头了跳出while循环
        return res













