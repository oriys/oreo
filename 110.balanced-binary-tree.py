#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if abs(self.height(root.left)-self.height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def height(self, node: TreeNode) -> int:
        if node == None:
            return 0
        return max(self.height(node.left), self.height(node.right))+1
