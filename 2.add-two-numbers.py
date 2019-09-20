#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        result = l1
        carry = 0
        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            carry = tmp // 10
            l1.val = tmp % 10
            if l1.next is None or l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next

        if l1.next is None:
            l1.next = l2.next

        while carry != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            l1 = l1.next
            tmp = l1.val + carry
            l1.val = tmp % 10
            carry = tmp // 10
        return result


