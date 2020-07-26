class Solution:
  def reverse_String(self, s):
    left, right = 0,  len(s)-1
    while left < right:
      s[left], s[right] = s[right], s[left]
      left = left + 1
      right = right - 1

    return s

if __name__ == '__main__':
  test = Solution()

  lst_reverse = ["h","e", "l", "l" ,"o"]

  print(test.reverse_String(lst_reverse))
