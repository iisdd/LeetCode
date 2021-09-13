'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''

# 列表57.5%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        node = [root]
        while 1:
            next_layer = []
            cur_layer = []
            for i in node:
                if i == None:
                    continue
                cur_layer.append(i.val)
                next_layer.append(i.left)
                next_layer.append(i.right)
            if cur_layer == []:
                return res
            res.append(cur_layer)
            node = next_layer




# 维护一个队列92.8%
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        res = []
        while queue != []:
            size = len(queue)
            tmp_val = []
            for _ in range(size):
                node = queue.pop(0)
                tmp_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp_val)
        return res
