#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(ans, l, r, n, max):
            if n == max:
                ans.append(l)
            for i in range(0, len(r)):
                helper(ans, l+[r[i]], r[:i]+r[i+1:], n+1, max)
        helper(ans, [], nums, 0, len(nums))
        return ans
