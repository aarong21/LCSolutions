class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m,n = len(grid), len(grid[0])

        # q = []
        # seen = set() of indices
        # def bfs():
            # 
        # explore grid if not seen:
            # if 1, hit a bfs
            # if 0, continue adding neighbors
        m, n = len(grid), len(grid[0])
        ans = 0
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans
                