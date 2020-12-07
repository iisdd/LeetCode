'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

'''
# 效率96%,字典多用get,别直接查找
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['dd']
        dct = {'(':')', '{':'}', '[':']'}
        # 如果是左括号就进栈,不然就比较是不是栈顶对应的右括号
        for i in s:
            if i in dct:
                stack.append(i)
            elif i != dct.get(stack.pop(), None):
                return False
        if stack != ['dd']:
            return False
        return True







        
