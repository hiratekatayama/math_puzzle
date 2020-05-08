class Solution(object):
  def findMaxLength(self, nums):
    maxlen = 0
    for start in range(len(nums)):
      zeroes = 0
      ones = 0
      for end in range(start, len(nums)):
        if nums[end] == 0:
          zeroes += 1
        else:
          ones += 1
        if zeroes == ones:
          maxlen = max(maxlen, end - start + 1)

    return maxlen

  def findMaxLength_2(self,nums):
    arr = [-2]*(2 * len(nums) + 1)
    arr[len(nums)] = -1
    for i in range(len(nums)):
      maxlen = 0
      count = 0
      for i in range(len(nums)):
        count = count + (-1 if nums[i] == 0 else 1)
        if arr[count + len(nums)] >= -1:
          maxlen = max(maxlen, i - arr[count + len(nums)])
        else:
          arr[count + len(nums)] = i

    return maxlen

if __name__ == '__main__':
  input = [1,0]
  test = Solution()
  print(test.findMaxLength(input))
  print(test.findMaxLength_2(input))
