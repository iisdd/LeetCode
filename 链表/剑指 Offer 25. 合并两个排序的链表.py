'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
'''
# 用时77.2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 边界条件
        if not l1:
            return l2
        if not l2:
            return l1
        cur = l1 if l1.val < l2.val else l2
        res = ListNode(None)
        res.next = cur
        while l1 and l2:
            if l1.val < l2.val:
                next_node = l1.next
                cur.next = l1
                l1 = next_node
            else:
                next_node = l2.next
                cur.next = l2
                l2 = next_node
            cur = cur.next          # 推进
        # 结尾
        cur.next = l1 if l1 else l2
        return res.next


