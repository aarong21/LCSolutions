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

        # if n < 2:
        #     return 1
        # elif n < 3:
        #     return 2
        # lis = [0]*n
        # lis[0], lis[1] = 1, 2

        # for i in range(2, n):
        #     lis[i] = lis[i-1] + lis[i-2]
        # return lis[-1]