'''
统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0

提示：

0 <= n <= 5 * 106
'''
# 用时25.3%
class Solution:
    def countPrimes(self, n: int) -> int:
        # 从2开始到int(n**0.5),把每个数字的所有倍数涂成0
        if n <= 2:
            return 0
        res = [1 for _ in range(n)]
        res[0] = 0                                      # 对应因数0
        res[1] = 0                                      # 对应因数1
        for i in range(2, int(n**0.5)+1):               # 间隔
            for j in range(2*i, n, i):
                res[j] = 0
        return sum(res)


# 用时55.2%
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        res = [1 for _ in range(n)]
        res[0] = 0                                      # 对应因数0
        res[1] = 0                                      # 对应因数1
        for i in range(2, int(n**0.5)+1):               # 间隔
            # 改进点1:res[i]=0就跳过
            if res[i] == 0:                             # 例如2的倍数看过了,就不看4的倍数了
                continue
            for j in range(2*i, n, i):
                res[j] = 0
        return sum(res)




# 用时78.1%
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        res = [1 for _ in range(n)]
        res[0] = 0                                      # 对应因数0
        res[1] = 0                                      # 对应因数1
        up_limit = int(n**0.5)+1
        for i in range(2, up_limit):                    # 间隔
            if res[i]:                                  # 例如2的倍数看过了,就不看4的倍数了
                # 改进点2:用列表表达式代替for循环赋值
                res[2*i : n : i] = [0] * ((n-1)//i-1)   # 牛!!!
        return sum(res)



# 用时93.5%
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        res = [1]*n                                     # [x]*n的方法比[x for _ in range(n)]要快!!!
        res[0] = 0                                      # 对应因数0
        res[1] = 0                                      # 对应因数1
        up_limit = int(n**0.5)+1
        for i in range(2, up_limit):                    # 间隔
            if res[i]:                                  # 例如2的倍数看过了,就不看4的倍数了
                # 改进点3:从i^2开始赋值,Ex:i=4时,i*2已经被2搞掉,i*3被3搞掉,所以从4*4开始
                res[i**2 : n : i] = [0] * ((n-1-i**2)//i+1)
        return sum(res)




