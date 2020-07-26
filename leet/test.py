class Solution(object):
  def reverse_String(self, s):
    left, right = 0, len(s) - 1
    while left > right:
      s[left], s[right] = s[right], s[left]
      left, right = left + 1, right - 1

    return s

if __name__ == '__main__':
  pass
