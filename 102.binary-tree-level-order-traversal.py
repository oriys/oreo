#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            n = len(q)
            ans.append(list(map(lambda z: z.val, q)))
            for _ in range(n):
                node = q[0]
                q = q[1:]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
