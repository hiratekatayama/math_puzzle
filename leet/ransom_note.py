import collections

class Solution(object):
  def canConstruct(self, ransomNote, magazine):
    dic = collections.Counter(magazine)
    for char in ransomNote:
      if char not in dic:
        if char not in dic:
          return False
        else:
          dic[char] -= 1
          if dic[char] < 0:
            return False
      return True

  def canConstruct_2(self, ransomNote, magazine):
    counter1 = collections.Counter(ransomNote)
    counter2 = collections.Counter(magazine)

    for c in counter1:
      print(c)
      if c not in counter2 or counter1[c] > counter2[c]:
        return False
    return True

  def canConstruct_3(self, ransomNote, magazine):
    dic = collections.Counter(magazine)
    for char in ransomNote:
      if char not in dic:
        return False
      else:
        dic[char] -= 1
        if dic[char] < 0:
          return False
    return True

if __name__ == '__main__':
  test = Solution()
  ransomNote = "ab"
  magazine = "aab"

  print(test.canConstruct(ransomNote, magazine))
  print(test.canConstruct_2(ransomNote, magazine))
  print(test.canConstruct_3(ransomNote, magazine))
