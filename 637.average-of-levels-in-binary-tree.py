#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from functools import reduce


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            n = len(q)
            ans.append(reduce(lambda x, y: x + y, list(map(lambda z: z.val, q)), 0)/n)
            for _ in range(n):
                node = q[0]
                q = q[1:]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
