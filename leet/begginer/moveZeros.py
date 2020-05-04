class Solution(object):
  def moveZeroes(self, nums):
    n = len(num)

    int numZeros = 0
    for i in n:
      numZeros += (nums[i] == 0)

    ans = []
    for i in n:
      if nums[i] != 0:
        ans.add(nums[i])

  def moveZeroes_2(self, nums):
    zero = 0
    for i in range(len(nums)):
      if nums[i] != 0:
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1
    return nums

if __name__ == '__main__':
  nums = [1,0,0,3,12]
  test = Solution()
  print(test.moveZeroes(nums))
