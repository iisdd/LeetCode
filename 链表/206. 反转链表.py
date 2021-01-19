'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
# 用时93.4%, 普通翻转

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res_node = None                     # 倒着来
        while head:
            tmp = head
            head = head.next
            tmp.next = res_node
            res_node = tmp
        return res_node

# 用时58.2, 双指针法
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = None
        pre = head
        while pre:
            tmp = pre.next
            pre.next = cur
            cur = pre
            pre = tmp
        return cur










        
