class Solution(object):
  def min_max(self, x, y):
    r = y^((x^y) &- (x<y))
    return r

if __name__ == '__main__':
  test = Solution()
  print(test.min_max(10, 5))

# http://graphics.stanford.edu/~seander/bithacks.html#CopyIntegerSign
