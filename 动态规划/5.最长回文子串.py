'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''
# 中心扩散法O(n^2),用时64.0%,不用浪费空间
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:                   # 边界情况
            return s
        max_len = 1
        res = ''
        # 奇数长度情况
        for i in range(n):
            d = 0                   # 两边扩散的距离
            while i-d>=1 and i+d<=n-2 and s[i-d-1]==s[i+d+1]:
                d += 1
            if 2*d+1 >= max_len:
                max_len = 2*d+1
                res = s[i-d:i+d+1]
        # 偶数长度情况
        for i in range(n-1):        # 遍历两个字符串之间的间隙
            d = -1
            while i-d>=1 and i+d+1<=n-2 and s[i-d-1]==s[i+d+2]:
                d += 1
            if 2*d+2 >= max_len:
                max_len = 2*d+2
                res = s[i-d:i+d+2]
        return res

# 动态规划O(n^2),遍历首尾,判断是否为回文只需O(1),内存消耗O(n^2)
# 用时27.8%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        res = ''
        if n < 2:
            return s
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):                      # 奇数长度的初始情况
            dp[i][i] = 1                        # 1代表为回文
            max_len = 1
            res = s[i:i+1]
        for i in range(n-1):                    # 偶数长度的初始情况
            if s[i] == s[i+1]:  
                dp[i][i+1] = 1
                max_len = 2
                res = s[i:i+2]
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                if dp[i+1][j-1]==1 and s[i]==s[j]:
                    dp[i][j] = 1
                    if j-i >= max_len:
                        max_len = j-i
                        res = s[i:j+1]
        return res

