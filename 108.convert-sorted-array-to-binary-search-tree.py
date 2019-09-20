#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        _ = len(nums)
        __ = _ // 2
        root = TreeNode(nums[__])
        root.left = self.sortedArrayToBST(nums[:__])
        root.right = self.sortedArrayToBST(nums[__+1:])
        return root
