#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for value in nums:
            prev, cur = cur, max(prev + value, cur)
        return cur