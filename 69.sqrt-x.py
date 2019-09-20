#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        t = x
        while t * t > x:
            t = int(t / 2 + x / (2 * t))
        return t
        

