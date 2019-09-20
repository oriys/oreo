class Solution:
    def isUgly(self, num: int) -> bool:
        for n in [2, 3, 5]:
            while num and num % n == 0:
                num //= n
        return num == 1
