'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''
# 用时88%,在已有的链表上操作比拉一条新链表要快的多

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 先快慢指针找中点切开,再把右边一半reverse
        # 特殊情况
        if head == None or head.next == None:
            return head
        fast = head
        slow = head
        tmp = None                      # 用于左半边收尾
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow
            slow = slow.next
        if fast:                        # 长度为奇数
            tmp = slow
            slow = slow.next
        tmp.next = None                 # 左半边收尾
        pre = slow
        cur = slow.next
        pre.next = None                 # 右半边收尾
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
            
        # 现在两条子链表的头节点为head&pre,head长度大于等于pre
        res = head
        counter = 0
        while head or pre:
            if counter%2 == 0:
                next_node = head.next
                head.next = pre
                head = next_node
            else:
                next_node = pre.next
                pre.next = head
                pre = next_node
            counter += 1
        return res
            

        
            


        
