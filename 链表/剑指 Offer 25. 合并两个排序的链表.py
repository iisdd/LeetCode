'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
'''
# 92.5%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        head = res
        pos1 = l1
        pos2 = l2
        while pos1 and pos2:
            if pos1.val <= pos2.val:
                res.next = pos1
                pos1 = pos1.next
            else:
                res.next = pos2
                pos2 = pos2.next
            res = res.next
        if not pos1: res.next = pos2
        else: res.next = pos1
        return head.next



















