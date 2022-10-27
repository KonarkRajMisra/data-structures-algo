"""
Problem statement:
    Given a m * n matrix, an island is a group of 1's connected 4-directionally. 
    - Assume four edges of the grid are surrounded by water.
    - Area of island is the number of cells with a value 1 in the island.
    Return max area of island, if no island return 0
"""

class Island:
    def __init__(self, grid) -> None:
        self.grid = grid
    
    def maxAreaIsland(self):
        maxArea = 0
        visit = set()

        def dfs(i,j):
            # check for invalid conditions
            if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or (i,j) in visit or self.grid[i][j] == 0:
                return 0
            
            visit.add((i,j))
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        return maxArea

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

island = Island(grid)
maxArea = island.maxAreaIsland()
print(maxArea)

# Time Complexity: O(N*M)
# Space: O(N*M)