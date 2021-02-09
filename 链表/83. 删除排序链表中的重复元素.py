'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
'''
# 用时82.3%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur_node = next_node = head
        while cur_node:
            while next_node.next and next_node.val == next_node.next.val:       # 跳到重复的尾端
                next_node = next_node.next
            next_node = next_node.next                                          # 再前进一格
            cur_node.next = next_node
            cur_node = cur_node.next
        return head


