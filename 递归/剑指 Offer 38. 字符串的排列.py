'''
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 
限制：
1 <= s 的长度 <= 8
'''
# 方法一,用check列表去重
# 用时60.3%
class Solution:
    def permutation(self, s: str) -> List[str]:
        self.res = []
        list_s = list(s)
        list_s.sort()
        n = len(list_s)
        check = [0 for _ in range(n)]
        self.traceback(list_s, '', check, n)
        return self.res

    def traceback(self, li, tmp, check, n):
        if len(tmp) == n:
            self.res.append(tmp)
        else:
            for i in range(n):
                if check[i]:                            # 用过的元素跳过
                    continue
                if i>0 and li[i]==li[i-1] and check[i-1]==0:
                    # 当前元素与上一元素相同,且上一元素没用过,跳过
                    continue
                check[i] = 1                            # 征用该元素
                self.traceback(li, tmp+li[i], check, n)
                check[i] = 0                            # 释放该元素





