#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p, q = ListNode(-1), head
        p.next, head = head, p
        while q:
            while q.next and q.next.val == q.val:
                q = q.next
            p.next, p = q, q
            if q: q = q.next
        return head.next