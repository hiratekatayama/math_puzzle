import bisect

class Solution(object):
  def lastStoneWeight(self, stones):
    stones.sort()
    while len(stones) > 1:
      bisect.insort(stones, stones.pop() - stones.pop())
    return stones[0]

  def lastStoneWeight_2(self, stones):
    for i in range(len(stones)-1):
      stones.sort()
      stones.append(stones.pop() - stones.pop())
    return stones[0]

if __name__ == '__main__':
  input = [2,7,4,1,8,1]

  test = Solution()

  print(test.lastStoneWeight(input))
  print(test.lastStoneWeight_2(input))
