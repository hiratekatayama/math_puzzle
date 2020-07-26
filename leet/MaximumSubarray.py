class Solution(object):
  def maxSubArray(self, nums):
    if not nums:
      return None
    dp = [0] * len(nums)
    res = dp[0] = nums[0]

    for i in range(1, len(nums)):
      dp[i] = max(dp[i-1]+nums[i], nums[i])
      res = max(res, dp[i])

    return res

  def maxSubArray_2(self, nums):
    if not nums:
      return None
    loc = glo = nums[0]
    for i in range(1, len(nums)):
      loc = max(loc+nums[i], nums[i])
      glo = max(loc, glo)
    return glo


if __name__ == '__main__':
  input = [-2,1,-3,4,-1,2,1,-5,4]

  test = Solution()
  print(test.maxSubArray(input))
