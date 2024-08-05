class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        i = 2
        if n == 1:
            return one
        elif n == 2:
            return two
        
        while i < n:
            one, two = two, one+two
            i += 1
        return two