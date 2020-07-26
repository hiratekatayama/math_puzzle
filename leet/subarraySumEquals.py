class Solution(object):
  def subarraySumEquals(self, nums, k):
    count = 0
    for start in range(len(nums)):
      for end in range(start+1, len(nums)+1):
        print("start",start,"end",end)
        sum = 0
        for i in range(start, end):
          sum += nums[i]
          if sum == k:
            count += 1

    return count


if __name__ == '__main__':
  input = [1, 1, 1]
  k = 2

  test = Solution()
  print("last",test.subarraySumEquals(input, k))
