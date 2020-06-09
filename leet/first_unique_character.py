import collections

class Solution:

  def firstUniqChar(self, s):
    count = collections.Counter(s)

    for idx, ch in enumerate(s):
      print(idx, ch, count[ch])
      if count[ch] == 1:
        return idx

    return -1

if __name__ == '__main__':
  test = Solution()

  s = "loveleetcode"

  print(test.firstUniqChar(s))
