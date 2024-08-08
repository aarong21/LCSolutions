class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

            # mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if dfs(new_i, new_j, k + 1):
                    return True

            # change back to original value
            board[i][j] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
