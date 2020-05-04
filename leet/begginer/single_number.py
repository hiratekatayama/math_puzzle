class Solution(object):
  def singleNumber(self, nums):
    a = 0
    for i in nums:
      a ^= i
    return a

if __name__ == '__main__':
  num_list = [7,4,4]
  sol = Solution()
  print(sol.singleNumber(num_list))
