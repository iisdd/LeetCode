'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
提示：
树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
'''
# 效率83.0%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def loop(node):
            # 中序: 左根右
            if not node:
                return None
            loop(node.left)
            res.append(node.val)
            loop(node.right)
        loop(root)
        return res
