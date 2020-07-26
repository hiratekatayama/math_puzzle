class Solution(object):
  def search(self, nums, target):
    if not nums:
      return -1
    i = 0
    j = len(nums) - 1
    while i < j:
      mid = i + (j-i) // 2
      if nums[mid] == target:
        return mid
      if nums[i] == target:
        return i
      if nums[j] == target:
        return j
      elif nums[mid] > target:
        if target > nums[i]:
          j = mid - 1
        else:
          if nums[mid] >= nums[i]:
            i = mid + 1
          else:
            j = mid - 1
      else:
        if target < nums[i]:
          i = mid + 1
        else:
          if nums[mid] >= nums[i]:
            i = mid + 1
          else:
            j = mid - 1
    if nums[i] == target:
      return i

    return -1

  def search_2(self, nums, target):
    if not nums:
      return -1

    low, high = 0, len(nums) - 1

    while low <= high:
      mid = (low + high) / 2
      if target == nums[mid]:
        return mid

      if nums[low] < nums[mid]:
        if nums[low] <= target <= nums[mid]:
          high = mid - 1
        else:
          low = mid + 1
      else:
        if nums[mid] <= target <= nums[high]:
          low = mid + 1
        else:
          high = mid - 1

    return -1

if __name__ == '__main__':
  input = [4,5,6,7,0,1,2]
  target = 0
  test = Solution()

  print(test.search_2(input, target))
