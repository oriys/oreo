#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValid(self, node: TreeNode, left, right) -> bool:
        if node == None:
            return True
        if node.val <= left or node.val >= right:
            return False
        return self.isValid(node.left, left, node.val) and self.isValid(node.right, node.val, right)

    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        return self.isValid(root,  -9223372036854775808, 9223372036854775807)
