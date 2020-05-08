class Solution(object):
  def firstBadVersion(self, n): #linear scan
    for i in range(1,n):
      if isBadVersion(i):
        return i
    return n

  def firstBadVersion_2(self, n): #binary search
    left = 1
    right = n
    while left < right:
      mid = left + (right - left) / 2
      if isBadVersion(mid):
        right = mid
      else:
        left = mid + 1
    return left
