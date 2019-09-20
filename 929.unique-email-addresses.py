#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = ''.join(list(filter(lambda c: c != '.', local)))
            s.add(local+'@'+domain)
        return len(s)
