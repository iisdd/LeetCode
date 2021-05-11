'''
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：


输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：


输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：


输入：p = [1,2,1], q = [1,1,2]
输出：false
 

提示：

两棵树上的节点数目都在范围 [0, 100] 内
-104 <= Node.val <= 104
'''
# 效率95.7%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None: # 到头了才return True
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:          # 这里不能写成 if p.val==q.val : return True, 因为没到底
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

