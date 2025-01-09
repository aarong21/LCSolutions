class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        res = []

        going_up = True
        cur_row = cur_col = 0

        # run until array is full
        while len(res) != rows * cols:
            if going_up:
                while cur_col < cols and cur_row >= 0: # up and right
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == cols: # if on right side
                    cur_row += 2
                    cur_col -= 1
                else: # if on top
                    cur_row += 1
                going_up = False
            else:
                while cur_row < rows and cur_col >= 0: # down and left
                    res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                if cur_row == rows: # if on bottom
                    cur_row -= 1
                    cur_col += 2
                else: # if on right
                    cur_col += 1
                going_up = True
        return res
