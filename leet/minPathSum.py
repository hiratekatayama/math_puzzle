import math

class Solution(object):
  def minPathSum(self, grid):
    node_num = len(grid)

    unsearched_nodes = list(range(node_num)) #未探索ノード
    distance = [math.inf] * node_num #ノードごとの距離のテスト
    previous_nodes = [-1] * node_num #最短経路でそのノードの一つ前に到達するノードリスト
    distance[0] = 0

    def get_target_min_index(min_index, distance, unsearched_nodes):
      start = 0
      while True:
        index = distance.index(min_index, start)
        found = index in unsearched_nodes
        if found:
          return index
        else:
          start = index + 1

    while(len(unsearched_nodes) != 0):
      posible_min_distance = math.inf
      for node_index in unsearched_nodes:
        if posible_min_distance > distance[node_index]:
          posible_min_distance = distance[node_index]

  def dfs(self, grid, i, j):

    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

if __name__ == '__main__':
  input = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
      ]

  test = Solution()
  print(test.minPathSum(input))
