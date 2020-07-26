class Solution:
  def check(self, coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    if len(coordinates) == 2:
      return True

    if x1 - x2 != 0:
      m = (y2-y1)/(x1-x2)
    else:
      m = 2**31-1

    for x,y in coordinates[2:]:
      if x1-x == 0:
        if m != 2**31-1:
          return False
        else:
          continue
      if ((y-y1)/(x1-x)) != m:
        return False
    return True

if __name__ == "__main__":
  test = Solution()
  coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
  print(test.check(coordinates))

  coordinates2 = [[1,2],[2,3],[4,4],[4,5],[5,6],[6,7]]
  print(test.check(coordinates2))
