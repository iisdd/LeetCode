'''
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
 
示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"

提示：

1 <= s.length <= 104
s 由小写英文字母组成
'''
# 用时91.2%
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 只要有新来的和旧的比较,就想到用单调栈!
        # 需要一个集合来记录栈中已有元素
        # 还需要一个字典记录剩余元素数量,因为独苗不能pop
        from collections import Counter
        stack = []
        elements = set()
        counter = Counter(s)
        for i in s:
            if i not in elements:
                while stack and i<stack[-1] and counter[stack[-1]]>0:
                    elements.discard(stack.pop())
                elements.add(i)
                stack.append(i)
            counter[i] -= 1
        return ''.join(stack)
                    
                    
        
