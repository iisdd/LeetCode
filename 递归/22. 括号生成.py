'''
给出 n 代表生成括号的对数，请你写出一个函数，
使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
# 递归,用时89.0%
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def loop(l , r , tmp):                  # l,r分别代表剩余能用的左右括号
            if l == 0 and r == 0:               # 终止条件
                res.append(tmp)
            elif l == r:
                loop(l-1 , r , tmp+'(')
            else:
                if l > 0:                       # 还有左括号用
                    loop(l-1 , r , tmp+'(')
                    loop(l , r-1 , tmp+')')
                else:                           # 没有左括号了
                    loop(l , r-1 , tmp+')')
        loop(n , n , '')
        return res


# DP,用时89.0%
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 用动态规划来做,n的情况为:(p对括号)+q对括号
        # p+q=n-1,遍历所有p,q的情况即可
        dp = [[''], ['()']]                     # n=0,n=1的初始情况
        for i in range(1, n):                   # i=n-1
            cur_res = []
            for p in range(i+1):
                q = i-p
                for t1 in dp[p]:
                    for t2 in dp[q]:
                        cur_res.append('('+t1+')'+t2)
            dp.append(cur_res)
        return dp[-1]
              
            
