#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            n = len(q)
            ans.append(max(list(map(lambda z: z.val, q))))
            for _ in range(n):
                node = q[0]
                q = q[1:]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
