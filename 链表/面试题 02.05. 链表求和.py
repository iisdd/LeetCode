'''
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
'''
# 用时96.2%,做了一下午,我吐了,链表一定要搞pre和cur指针,不然搞不成器


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        res1, res2 = l1, l2
        carry = 0
        # 阶段1:公共部分
        while l1 and l2:
            num1 = l1.val
            num2 = l2.val
            l1.val = (num1 + num2 + carry) % 10         # 注意先算cur,再算carry,否则就不是上一位的carry了
            l2.val = l1.val                             # 算两份,谁长取谁
            carry = (num1 + num2 + carry) // 10
            pre1 = l1                                   # 记录一下上一节点
            pre2 = l2
            l1 = l1.next
            l2 = l2.next
        # 阶段2:多出来的部分
        if l1:                                          # l1长
            while l1 and carry:
                num1 = l1.val
                l1.val = (num1 + carry) % 10
                carry = (num1 + carry) // 10
                pre1 = l1
                l1 = l1.next
            if not l1:                                  # l1走到尽头,另一种情况是没有进位了
                if carry:                               # 阶段3:进位的尾巴
                    pre1.next = ListNode(1)
            return res1
        elif l2:                                        # l2长
            while l2 and carry:
                num2 = l2.val
                l2.val = (num2 + carry) % 10
                carry = (num2 + carry) // 10
                pre2 = l2
                l2 = l2.next
            if not l2:
                if carry:                               # 阶段3:进位的尾巴
                    pre2.next = ListNode(1)
            return res2
        else:                                           # l1,l2一样长
            if carry:                                   # 阶段3:进位的尾巴
                pre1.next = ListNode(1)
            return res1





