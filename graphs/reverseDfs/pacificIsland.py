"""
Problem Statement - An m x n island borders both the Pacific Ocean and Atlantic Ocean. 
    - Pacific Ocean touches the left and top edges.
    - Atlantic Ocean touches the right and bottom edges.
    - The matrix is partitioned into grid of square cells.
        - heights[r][c] represents the height above sea level.
        - Rain water can flow to neighboring cells in all four directions if:
            - the neighboring cell's height is less than or equal to current cell's height.

    Fundamental learning about this problem is reverse thinking:
        - Going from inside the grid to outside requires going from high to small to reach ocean
        - Looking from outside to inside requires thinking which cell inside can reach this cell, only strictly greater cells.
"""

class PacificAtlantic:
    def __init__(self, island) -> None:
        self.island = island
    
    def findPacificAtlantic(self):
        ROWS, COLS = len(self.island), len(self.island[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prev):
            # if out of bounds, visited, or if the value we are comming from is greater than previous value, as we are going from outside to inwards
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or self.island[r][c] < prev:
                return

            visit.add((r,c))
            dfs(r + 1, c, visit, self.island[r][c])
            dfs(r - 1, c, visit, self.island[r][c])
            dfs(r, c + 1, visit, self.island[r][c])
            dfs(r, c - 1, visit, self.island[r][c])

        # check which cells can reach pacific going from the first col
        # and check which cells can reach atlantic going from the last col
        for r in range(ROWS):
            dfs(r, 0, pacific, self.island[r][0])
            dfs(r, COLS - 1, atlantic, self.island[r][COLS - 1])

        # check which cells can reach pacific ocean going from first row
        # same for atlantic ocean last column
        for c in range(COLS):
            dfs(0, c, pacific, self.island[0][c])
            dfs(ROWS-1, c, atlantic, self.island[ROWS-1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res


island = PacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(island.findPacificAtlantic())

# Time: O(M*N)
# Space: O(M*N)