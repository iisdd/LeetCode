'''
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

注意：

给定的目标值 target 是一个浮点数
题目保证在该二叉搜索树中只会存在一个最接近目标值的数
示例：

输入: root = [4,2,5,1,3]，目标值 target = 3.714286

    4
   / \
  2   5
 / \
1   3

输出: 4
'''
# 用时97.4%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        d = float('inf')                            # 节点与target的距离
        res = root.val
        while root.val != None:
            if abs(root.val - target) <= d:         # 更新new record
                d = abs(root.val - target)
                res = root.val
            if root.val > target and root.left:     # 节点大于目标值,移动到左节点
                root = root.left
            elif root.val < target and root.right:  # 节点小于目标值,移动到右节点
                root = root.right
            else:                                   # 移动到底了
                return res
        




















        
