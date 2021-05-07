'''
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
'''
# 效率82.9%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def loop(node):
            # 前序: 根左右
            if not node:
                return None
            res.append(node.val)
            loop(node.left)
            loop(node.right)
        loop(root)
        return res