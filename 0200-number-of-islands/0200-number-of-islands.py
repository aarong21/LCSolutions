class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] != '1':
                return
            grid[row][col] = '0'
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        for i in range(m): # rows
            for j in range(n): # cols
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        
        return count

