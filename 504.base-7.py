#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = []
        sign = num >= 0
        num = abs(num)
        while num != 0:
            ans.append(num % 7)
            num //= 7
        return ("" if sign else "-") + "".join(map(str, ans[::-1]))
