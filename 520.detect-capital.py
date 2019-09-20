#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#


class Solution:
    def exceptUpper(self, word: str)->bool:
        if len(word) == 0:
            return True
        if word[0].islower():
            return False
        return self.exceptUpper(word[1:])

    def exceptLower(self, word: str)->bool:
        if len(word) == 0:
            return True
        if word[0].isupper():
            return False
        return self.exceptLower(word[1:])

    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            return self.exceptUpper(word[1:]) or self.exceptLower(word[1:])
        else:
            return self.exceptLower(word[1:])
