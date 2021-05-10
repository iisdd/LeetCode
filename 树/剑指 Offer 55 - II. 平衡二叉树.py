'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

限制：

0 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/
'''
# 效率68.7%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 递归求节点深度
        def loop(cur_d, node):
            # cur_d: 当前深度, node: 当前所处节点
            if node.left == None:                   # 左边到底了
                left = cur_d
            else:
                left = loop(cur_d + 1, node.left)
            if node.right == None:                  # 右边到底了
                right = cur_d
            else:
                right = loop(cur_d + 1, node.right)
            if left == -1 or right == -1:           # 子树不平衡
                return -1
            if abs(left - right) > 1: return -1     # 当前节点不平衡

            return max(left, right)
        if not root: return True
        return loop(0, root) != -1
