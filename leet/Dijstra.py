class Solution(object):
  def minPathSum(self, grid):
    r, c = len(grid), len(grid[0])
    heap = [(grid[0][0], (0,0))]
    visit = set()
    while heap:
      s, (i, j) = heapq.heappop(heap)
      if (i, j) in visit:
        continue
      visit.add((i, j))
      for x, y in ((i+1, j), (i, j+1)):
        if x < r and y < c:
          s1 = s + grid[x][y]
          heapq.heappush(heap, (s1, (x,y)))
          if x == r-1 and y == c-1:
            return s1
    return s

  def minPathSum(self, grid):
    if not grid:
      return 0

    m, n = len(grid[0]), len(grid)
    dp = [[float("inf")] * (m + 1) for i in range(n + 1)]
    dp[0][1], dp[1][0] = 0, 0

    for i in range(1, n + 1):
      for j in range(1, m + 1):
        dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]

if __name__ == '__main__':
  input = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
      ]

  test = Solution()
  print(test.minPathSum(input))
