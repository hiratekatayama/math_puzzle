class Solution(object):
  def isHappy(self, n): #simple algorithm
    stop = {1}
    while n not in stop:
      stop.add(n)
      n = sum(int(d)**2 for d in str(n))

    return n == 1

  def isHappy_2(self, n): #cycle algorithm
    s = lambda n: sum(int(d)**2 for d in str(n))
    m = s(n)
    while m != n:
      n, m = s(n), s(s(m))

    return n == 1


if __name__ == '__main__':
  num = 19
  a = Solution()
  print(a.isHappy(num))
  print(a.isHappy_2(num))
