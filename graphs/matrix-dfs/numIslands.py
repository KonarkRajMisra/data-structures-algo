"""
Problem statement:
    Given a m*n 2D grid, which represents 1's (land) and 0's (water) return the number of islands.
    - An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    - You may assume all four edges of the grid are surrounded by water.
"""

class Island:
    def __init__(self, grid) -> None:
        self.grid = grid
    
    def numIslands(self):
        visit = set()
        res = 0
        # Iterate through the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "1":
                    res += self.dfs(i,j, visit)
        return res

    def dfs(self,i,j,visit):
        # if invalid, return
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] == "0" or (i,j) in visit:
            return 0
        visit.add((i,j))
        self.dfs(i+1,j,visit)
        self.dfs(i-1,j,visit)
        self.dfs(i,j+1,visit)
        self.dfs(i,j-1,visit)
        return 1

exampleOne = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
islandOne = Island(exampleOne)

exampleTwo = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
islandTwo = Island(exampleTwo)
print(islandOne.numIslands())
print(islandTwo.numIslands())