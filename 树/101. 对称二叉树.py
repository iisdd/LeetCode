'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树[1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
'''

# 广度优先95%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        node = [root]
        while 1:
            next_layer = []
            next_value = []
            for i in node:
                if i != None:
                    next_layer.append(i.left)
                    if i.left != None:
                        next_value.append(i.left.val)
                    else:
                        next_value.append(None)
                    next_layer.append(i.right)
                    if i.right != None:
                        next_value.append(i.right.val)
                    else:
                        next_value.append(None)
            if next_value == []:
                return True
            if self.jugde(next_value):
                print(next_value)
                return False
            node = next_layer
    def jugde(self, li):
        if li == li[::-1]:
            return False
        return True



# 深度优先95%且不占内存

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            elif left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)