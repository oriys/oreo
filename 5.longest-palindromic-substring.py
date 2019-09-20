#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        ans = ''
        for i in range(len(s)):
            res = palindrome(s, i, i)
            ans = res if len(res) > len(ans) else ans
            res = palindrome(s, i, i+1)
            ans = res if len(res) > len(ans) else ans
        return ans
