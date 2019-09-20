#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

import math


class Solution:
    def isPrime(self, n: int) -> bool:
        for i in range(2, math.floor(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count
