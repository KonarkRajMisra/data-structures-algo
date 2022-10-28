"""
Problem Statement - Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4 directionally surrounded by 'X'.
    - A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
class SurroundedRegions:
    def __init__(self, regions) -> None:
        self.regions = regions

    def solve(self):
        # Reverse thinking
        # O's located on the edge of the matrix cannot be converted into X's as they are not 4 directionally populated by X's
        ROWS,COLS = len(self.regions), len(self.regions[0])
        def dfs(r,c,visit):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or self.regions[r][c] != 'O':
                return
            self.regions[r][c] = '#'
            visit.add((r,c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

        visit = set()
        # Check all the cells on the edges, if they are O, convert them to wild card #
        for r in range(ROWS):
            for c in range(COLS):
                if (r in (0, ROWS - 1) or c in (0, COLS - 1)) and self.regions[r][c] == 'O':
                    dfs(r, c, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if self.regions[r][c] == 'O':
                    self.regions[r][c] = 'X'
        
        for r in range(ROWS):
            for c in range(COLS):
                if self.regions[r][c] == '#':
                    self.regions[r][c] = 'O'

regions = SurroundedRegions([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
regions.solve()
print(regions.regions)

             