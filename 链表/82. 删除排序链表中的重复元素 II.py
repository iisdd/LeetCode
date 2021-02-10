'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
'''
# 用时94.6%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = cur_node = self.push(head)
        if not res:                                                     # 特殊情况,空链表或全是重复的
            return res
        while cur_node and cur_node.next:
            next_node = self.push(cur_node.next)
            cur_node.next = next_node
            cur_node = cur_node.next
        return res

    def push(self, cur_node):
        if cur_node and cur_node.next and cur_node.val == cur_node.next.val:         # 有重复的向前推进
            while cur_node.next and cur_node.val == cur_node.next.val:
                cur_node = cur_node.next
            return self.push(cur_node.next)                             # 防止下一段也是连续重复的
        else:                                                           # 无重复直接录用
            return cur_node


