'''
返回与给定的前序和后序遍历匹配的任何二叉树。

pre和post遍历中的值是不同的正整数。

示例：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]

提示：

1 <= pre.length == post.length <= 30
pre[]和post[]都是1, 2, ..., pre.length的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
'''
# 62.8%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        else:
            # 左子树的根节点
            l_idx = postorder.index(preorder[1])
            root.left = self.constructFromPrePost(preorder[1:l_idx+2], postorder[:l_idx+1])
            root.right = self.constructFromPrePost(preorder[l_idx+2:], postorder[l_idx+1:-1])
            return root















