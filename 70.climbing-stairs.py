class Solution:
    def climbStairs(self, n: int) -> int:
        one,two,cur=1,1,1
        for _ in range(2,n+1):
            cur=one+two
            two=one
            one=cur
        return cur