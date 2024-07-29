class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # initialize 2d array to store path values
        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        # fill first row
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            # fill first col
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        # fill out rest of array using values above and from left
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[rows-1][cols-1]