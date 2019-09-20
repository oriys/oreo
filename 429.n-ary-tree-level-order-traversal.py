#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# class Node:
#    def __init__(self, val, children):
#        self.val = val
#        self.children = children
# 
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                if node.children:
                    for child in node.children:
                        q.append(child)
        return ans
