class Solution(object):
  def numIslands(self, grid):
    islands = 0
    visited = set()

    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == "1" and (row, col) not in visited:
          islands += 1
          self.dfs(grid, row, col, visited)

    return islands

  def dfs(self, grid, row, col, visited):
    if (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and (row, col) not in visited and grid[row][col] == "1"):
      visited.add((row,col))
      self.dfs(grid, row+1, col, visited)
      self.dfs(grid, row-1, col, visited)
      self.dfs(grid, row, col+1, visited)
      self.dfs(grid, row, col-1, visited)

if __name__ == '__main__':
  input = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
      ]
  test = Solution()
  print(test.numIslands(input))
