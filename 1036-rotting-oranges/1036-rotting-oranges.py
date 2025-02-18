from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        count = 0

        # puts rotten oranges in queue
        # counts total fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    count += 1

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        minutes = 0

        while queue and count > 0:
            minutes += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for h,v in directions:
                    newx, newy = x + h, y + v
                    if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == 1:
                        grid[newx][newy] = 2 # rot spread
                        queue.append((newx,newy))
                        count -= 1
        return minutes if count == 0 else -1