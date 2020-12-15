'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？
 
示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。

提示：

链表中节点的数目范围在范围 [0, 10^4] 内
-10^5 <= Node.val <= 10^5
pos 的值为 -1 或者链表中的一个有效索引
'''

# 用时5%...我吐了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:       # 长度为1或0
            return None
        # 先要求出环的长度,快慢指针
        fast = head
        slow = head
        while fast != None:
            fast = fast.next
            if fast == None:
                return None
            fast = fast.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None:
            return None
        len_loop = 1
        fast = fast.next.next
        slow = slow.next
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            len_loop += 1
        # 现在开始找环的入口
        pos = 0
        while 1:
            curNode = head
            for i in range(pos):                    # 尝试第i个节点
                curNode = curNode.next
            tryNode = curNode
            for i in range(len_loop):
                tryNode = tryNode.next
            if tryNode == curNode:                  # 走了一圈又走回来了
                return curNode
            pos += 1
                
        
        

# 改进版用时90.2%!!!
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:       # 长度为1或0
            return None
        # 先要求出环的长度,快慢指针
        fast = head
        slow = head
        while fast != None:
            fast = fast.next
            if fast == None:
                return None
            fast = fast.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None:
            return None
        # 这里有一个非常神妙的技巧,链表分两段,a+b,a为环外长度,b为环内
        # 假设slow走过的距离为s,fast走过2s, 2s = s+nb(fast比slow多走了几圈)
        # 所以s = nb!!! 那么从起点走到环口需要走nb+a步
        # 胜利的方程式已经齐备!!! 让slow(差a步到)和head(差a步到)同时走
        # 汇合的点就是环口的位置
        while head != slow:
            head = head.next
            slow = slow.next
        return head

















        
