class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        flag = 1 if x >= 0 else -1
        x = abs(x)
        while x:
            y = y * 10 + (x % 10)//1
            x //= 10
        y *= flag
        return y if y < 2147483648 and y >= -2147483648 else 0
