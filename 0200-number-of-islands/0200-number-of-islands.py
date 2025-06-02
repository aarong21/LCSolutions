class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=='0':
                return
            grid[r][c] = '0'
            dfs(r+1,c) # down
            dfs(r-1,c) # up
            dfs(r,c+1) # right
            dfs(r,c-1) # left
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i,j)
        return num_islands

