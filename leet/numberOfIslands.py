class Solution(object):
  def numIslands(self, grid):
    count = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == "1":
          self.dfs(grid, i, j)
          count += 1

    return count
  
  def dfs(self, grid, i, j):
    if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == "0":
      return
    grid[i][j] = "0"
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)

if __name__ == '__main__':
  input = [
  ["1","1","0","0","0"],
  ["1","1","1","0","1"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"],
  ]

  test = Solution()
  print(test.numIslands(input))
