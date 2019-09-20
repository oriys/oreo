#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#


class Solution:
    def dayOfYear(self, date: str) -> int:
        ymd = date.split('-')
        y, m, d = int(ymd[0]), int(ymd[1]), int(ymd[2])
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        result = sum(days[0:m-1])+d
        if leap and m > 2:
            result += 1
        return result
