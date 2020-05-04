class Solution(object):
  def maxSubArray(self, nums): #Simple
    max_num = 0
    for i in range(1,len(nums)+1):
      for j in range(len(nums)-i+1):
        sum_nums = 0
        list_sum = []
        for k in range(j, i+j):
          list_sum.append(nums[k])
          sum_nums = sum(list_sum)
        if max_num < sum_nums:
          max_num = sum_nums

  def maxSubArray_2(self, nums): #DP problem O(n)
    if not nums:
      return None
    dp = [0]*len(nums)
    res = dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = max(dp[i-1]+nums[i], nums[i])
      res = max(res, dp[i])
    return res

  def maxSubArray_3(self, nums):
    if not nums:
      return None

    dp = [0]*len(nums)
    res = dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = max(dp[i-1]+nums[i], nums[i])
      #res = max(res, dp[i])
    return dp[i]


if __name__ == '__main__':
  input = [-2,1,-3,4,-1,2,1,-5,4]
  a = Solution()
  print(a.maxSubArray_3(input))
