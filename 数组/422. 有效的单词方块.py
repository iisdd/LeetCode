'''
给你一个单词序列，判断其是否形成了一个有效的单词方块。

有效的单词方块是指此由单词序列组成的文字方块的 第 k 行 和 第 k 列 (0 ≤ k < max(行数, 列数)) 所显示的字符串完全相同。

注意：

给定的单词数大于等于 1 且不超过 500。
单词长度大于等于 1 且不超过 500。
每个单词只包含小写英文字母 a-z。
 

示例 1：

输入：
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

输出：
true

解释：
第 1 行和第 1 列都是 "abcd"。
第 2 行和第 2 列都是 "bnrt"。
第 3 行和第 3 列都是 "crmy"。
第 4 行和第 4 列都是 "dtye"。

因此，这是一个有效的单词方块。
 

示例 2：

输入：
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

输出：
true

解释：
第 1 行和第 1 列都是 "abcd"。
第 2 行和第 2 列都是 "bnrt"。
第 3 行和第 3 列都是 "crm"。
第 4 行和第 4 列都是 "dt"。

因此，这是一个有效的单词方块。
 

示例 3：

输入：
[
  "ball",
  "area",
  "read",
  "lady"
]

输出：
false

解释：
第 3 行是 "read" ，然而第 3 列是 "lead"。

因此，这 不是 一个有效的单词方块。
'''
# 用时40.8%
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        def column(n):          # 取出第n列的字母
            n_c = ''
            for i in words:
                if len(i) > n:
                    n_c += i[n]
            return n_c
        m = len(words)
        for i in range(m):
            if words[i] != column(i):
                return False
        return True


# 用抛出异常试一试,一个字母一个字母的看
# 用时67.4%
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = len(words)
        try:
            for i in range(m):
                n = len(words[i])
                for j in range(n):
                    if words[i][j] != words[j][i]:
                        return False
            return True
        except:                         # 长度不对称
            return False



