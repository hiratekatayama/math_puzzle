class Solution(object):
  def prisonAfterNDays(self, cells, N):
    seen = {str(cells): N}
    while N:
      seen.setdefault(str(cells), N)
      N -= 1
      cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1,7)] + [0]
      if str(cells) in seen:
        N %= seen[str(cells)] - N
    return cells

  def Find_the_loop_pattern(self, cells, N):
    N -= int(max(N-1,0) / 14 * 14)
    for i in range(N):
      cells = [0] + [cells[i-1]^cells[i+1] ^ 1 for i in range(1,7)] + [0]
    return cells

  def prinsonAfterDays(self, cells, N):
    if N > 14:
      N = N%14

    if N%14 == 0:
      N = 14

    for i in range(1, N+1):
      temp = [0]*len(cells)
      for i in range(1, len(cells)-1):
        if cells[i-1] == cells[i+1]:
          temp[i] = 1
        else:
          temp[i] = 0
      cells = temp
    return cells

if __name__ == '__main__':
  test = Solution()
  cells = [1,0,0,1,0,0,1,0]
  N = 1000000000

  print(test.prisonAfterNDays(cells, N))
  print(test.Find_the_loop_pattern(cells, N))
