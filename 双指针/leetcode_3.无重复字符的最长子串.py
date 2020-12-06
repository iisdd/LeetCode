'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
# 用时93%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针法,维护一个字典储存两个指针中间的内容
        n = len(s)
        if n < 2:
            return len(s)
        l, r = 0, 1
        res = 1
        dct = {s[0]:0}                  # 字典查找效率高
        while r < n:
            if s[r] in dct:
                if dct[s[r]] >= l:      # 被夹在中间就移动左指针
                    l = dct[s[r]]+1
                dct[s[r]] = r
                r += 1
            else:
                dct[s[r]] = r
                r += 1
            res = max(res, r-l)
        return res                      # 可能第一种情况r>n结束循环了




        
