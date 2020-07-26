class Solution(object):
  def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      l, r = i+1, len(nums)-1
      while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0:
          l += 1
        elif s > 0:
          r -= 1
        else:
          res.append((nums[i], nums[l], nums[r]))
          while l < r and nums[l] == nums[l+1]:
            l += 1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
          l += 1; r -= 1
    return res

  def threeSum_2(self,nums):
    nums.sort()
    i, N, result = 0, len(nums), []
    while i < N-2:
      j, k = i+1, N-1
      while j < k:
        Sum = nums[i] + nums[j] + nums[k]
        if not Sum:
          result.append([nums[i], nums[j], nums[k]])
          while j < k and nums[j] == nums[j+1]: j += 1
          j += 1
          while j < k and nums[k] == nums[k - 1]: k -= 1
          k -= 1
        elif Sum < 0:
          while j < k and nums[j] == nums[j+1]: j += 1
          j += 1
        else:
          while j < k and nums[k] == nums[k-1]: k -= 1
          k -= 1
      while i < N-2 and nums[i] == nums[i+1]: i += 1
      i += 1
    return result

if __name__ == '__main__':
    test = Solution()
    nums = [-1,0,1,2,-1,-4]

    print(test.threeSum(nums))
    print(test.threeSum_2(nums))
