#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#


class Solution:
    def numTrees(self, n: int) -> int:
        result = 1
        for i in range(n+1, 2*n+1):
            result = result*1//(i-n)
        return result//(n+1)
