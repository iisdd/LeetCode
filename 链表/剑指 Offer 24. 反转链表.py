'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 
限制：

0 <= 节点个数 <= 5000
'''
# 用时100%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prepre = None
        pre = head
        while pre:
            cur = pre.next
            pre.next = prepre
            prepre = pre
            pre = cur
        return prepre
