class Solution(object):
  def subarraySum_bruteforce(self, nums, k):
    count = 0
    for start in range(len(nums)):
      sum = 0
      for end in range(start, len(nums)):
        sum += nums[end]
        if (sum == k):
          count += 1

    return count

  def subarraySum_cumulativesum(self, nums, k):
    count = 0
    sum = [0] * (len(nums)+1)
    sum[0] = 0
    for i in range(1,len(nums)+1):
      sum[i] = sum[i-1] + nums[i-1]
    for start in range(len(nums)):
      for end in range(start+1, len(nums)+1):
        if sum[end] - sum[start] == k:
          count += 1

    return count

  def subarray_withoutspace(self, nums, k):
    count = 0
    for start in range(len(nums)):
      sum = 0
      for end in range(start, len(nums)):
        sum += nums[end]
        if sum == k:
          count += 1

    return count

  def subarray_hashmap(self, nums, k):
    count = 0
    sum = 0

    map = {}
    map[0] = 1
    for i in range(len(nums)):
      sum += nums[i]
      if sum-k in map:
        count += map[sum-k]
      map[sum] = map.get(sum,0)+1
      print(map)

    return count


if __name__ == '__main__':
  nums = [1,1,1]
  k = 2

  code = Solution()
  #print(code.snubarraySum_bruteforce(nums, k))
  #print(code.subarraySum_cumulativesum(nums, k))
  #print(code.subarray_withoutspace(nums, k))
  print(code.subarray_hashmap(nums, k))
