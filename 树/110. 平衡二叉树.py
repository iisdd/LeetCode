'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：

输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true
 

提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104
'''
# 效率93.5%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def loop(node):
            if node == None:            # 到底了,返回树的深度
                return 0
            left = loop(node.left)
            right = loop(node.right)
            if left==-1 or right==-1:   # 继承子树的不平衡
                return -1
            if abs(left - right) > 1:   # 该节点不平衡
                return -1
            return 1+max(left, right)

        return loop(root) != -1

















