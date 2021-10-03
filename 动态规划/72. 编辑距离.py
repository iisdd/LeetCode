'''
给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
'''
# 递归超时,对word1每个位置都试三种操作看最后能不能变成word2,复杂度O(3^n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res = []
        def loop(s1, s2, count):
            if s1 == '' or s2 == '':
                count += len(s1) + len(s2)
                res.append(count)
            elif s1[0] == s2[0]:
                loop(s1[1:], s2[1:], count)
            else:
                # 插入
                loop(s1[:], s2[1:], count+1)
                # 删除
                loop(s1[1:], s2[:], count+1)
                # 替换
                loop(s1[1:], s2[1:], count+1)
        loop(word1, word2, 0)
        return min(res)






# 75%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[n+m for _ in range(m+1)] for _ in range(n+1)]  # dp[i][j]代表word1[:i]变成word2[:j]最少需要多少次操作
        dp[0][0] = 0
        for i in range(1, m+1):    # word2删光
            dp[0][i] = i
        for i in range(1, n+1):    # word1删光
            dp[i][0] = i

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    # 插入:dp[i+1][j]+1, 删除:dp[i][j+1]+1, 替换:dp[i][j]+1
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
        return dp[-1][-1]
