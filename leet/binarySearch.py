class Solution(object):
  def binary_search(self, list, target):
    result = -1
    left = 0
    right = len(list) - 1
    i = 0

    while left <= right:
      mid = (left + right) / 2
      if list[mid] == target:
        result = mid
        break
      elif list[mid] < target:
        left = mid + 1
      else:
        right = mid - 1

      i += 1

    return result


if __name__ == '__main__':
  num_list = [1,3,4,5,7,9,12,14,17]
  target = 12

  test = Solution()
  print(test.binary_search(num_list, target))
