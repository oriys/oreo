#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        d = {}
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            if A[i] != B[i]:
                d[i] = [A[i], B[i]]
        if len(d) > 2 or len(d) == 1:
            return False
        elif len(d) == 2:
            a, b = d.values()
            return a == b[::-1]
        else:
            return len(set(A)) != len(A)
