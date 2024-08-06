class Solution:
    def uniquePaths(self, m: int, n: int, memo = None) -> int:
        if memo is None:
            memo = {}
        if (m,n) in memo:
            return memo[(m,n)]
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        result = (self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo))
        memo[(m,n)] = result
        return result