#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        i, result = 0, 0
        while i < n:
            nums[result] = nums[i]
            result += 1
            j = i + 1
            while j < n and nums[j] == nums[j - 1]:
                j += 1
            i = j
        return result
