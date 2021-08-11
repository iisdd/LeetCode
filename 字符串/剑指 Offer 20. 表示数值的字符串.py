'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：
1.若干空格
2.一个小数或者整数
3.（可选）一个'e'或'E'，后面跟着一个整数
4.若干空格

小数（按顺序）可以分成以下几个部分：
1.（可选）一个符号字符（'+' 或 '-'）
2.下述格式之一：
    1.至少一位数字，后面跟着一个点 '.'
    2.至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
    3.一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
1.（可选）一个符号字符（'+' 或 '-'）
2.至少一位数字

部分数值列举如下：

["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：

["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]

示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = "   .1  "
输出：true


提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。
'''
# 92.6%
class Solution:
    def isNumber(self, s: str) -> bool:
        def isint(s):                       # 判断是否为整数
            if not s: return False
            if s[0] == '-' or s[0] == '+': s = s[1:]
            if not s: return False
            return s.isdigit()

        def isfloat(s):
            if not s: return False
            if s[0] == '-' or s[0] == '+': s = s[1:]
            if not s: return False
            if s.count('.') != 1: return False
            part1, part2 = s.split('.')
            if part1.isdigit() and part2 == '':
                return True
            elif part1.isdigit() and part2.isdigit():
                return True
            elif part1 == '' and part2.isdigit():
                return True
            else:
                return False

        # 先去掉前后空格
        s = s.strip()
        if s.count('e') == 1:
            part1, part2 = s.split('e')
        elif s.count('E') == 1:
            part1, part2 = s.split('E')
            print(part1, part2)
        else:
            return isint(s) or isfloat(s)
        return (isint(part1) or isfloat(part1)) and (isint(part2))
