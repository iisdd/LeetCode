'''给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
'''
# 效率61.7%, 这个可以有三合一的写法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def loop(node):
            # 后序: 左右根
            if not node:
                return None
            loop(node.left)
            loop(node.right)
            res.append(node.val)
        loop(root)
        return res