class Solution(object):
  def subsets(self, nums):
    result = []

    nums = list(sorted(nums))
    self.helper(nums, 0, [], result)

    return result

  def helper(self, nums, start_index, subset, result):
    result.append(list(subset))

    for i in range(start_index, len(nums)):
      subset.append(nums[i])

      self.helper(nums, i+1, subset, result)

      subset.pop()

  def subsets_2(self, nums):
    def backtracing(first=0, curr=[]):
      for i in range(first, len(nums)):
        curr.append(nums[i])
        backtracing(i+1, curr)
        curr.pop()

    result = []
    n = len(nums)
    for k in range(n+1):
      backtracing()
    return output


if __name__ == '__main__':
  test = Solution()
  nums = [1,2,3]
  check = test.subsets(nums)
  print(check)
