'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''
# 用时94.5%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 空链表
        if not head:
            return None
        # 找反转段
        cur, pre = head, None
        while m > 1:
            pre = cur
            cur = cur.next
            m, n = m-1, n-1
        mid1 = cur                      # 中间段的开头(翻转后变为结尾)
        left = pre                      # 左边一段的结尾
        while n:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
            n -= 1
        if left:
            left.next = pre
        else:
            head = pre
        mid1.next = cur
        return head

        















        
