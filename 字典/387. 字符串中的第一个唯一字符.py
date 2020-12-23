'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
'''
# 用时77.3%
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for idx, val in enumerate(s):
            if val in dct:
                dct[val] = -1
            else:
                dct[val] = idx
        res = len(s)
        for i in dct.values():
            if i >= 0 and i < res:
                res = i
        return res if res!=len(s) else -1

