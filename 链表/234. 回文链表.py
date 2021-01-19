'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''
# 用时7.1%, 鬼才写法,又超时又用了内存...

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 特殊情况
        if head == None:
            return True
        # 先翻转一下再同步遍历看看是否一致
        forward = head
        backward = ListNode(head.val)
        while head.next:
            head = head.next
            cur_node = ListNode(head.val)
            cur_node.next = backward
            backward = cur_node
        while backward:
            if backward.val != forward.val:
                return False
            backward = backward.next
            forward = forward.next
        return True


# 用时82.6%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 特殊情况
        if head==None or head.next==None:
            return True
        # 快慢指针法将慢指针遍历的前半部分翻转
        fast = head
        slow = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            # 翻转部分
            next_node = slow.next
            slow.next = pre
            pre = slow
            slow = next_node

        if fast:                        # 长度为奇数
            slow = slow.next
        while slow and pre:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
            
        
        














        
