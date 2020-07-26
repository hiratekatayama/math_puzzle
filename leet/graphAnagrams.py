#理解できていない
# 辞書で管理しているっぽい

import collections

class Solution(object):
  def groupAnagrams(self, strs): # categorize by sorted string
    ans = collections.defaultdict(list)
    for s in strs:
      ans[tuple(sorted(s))].append(s)
    return ans.values()

  def groupAnagrams_2(self, strs): # categorize by count
    ans = collections.defaultdict(list)
    for s in strs:
      count = [0]*26
      for c in s:
        count[ord(c)-ord('a')] += 1
      ans[tuple(count)].append(s)
    return ans.values()


if __name__ == '__main__':
  num = ["eat", "tea", "tan", "ate", "nat", "bat"]
  
  test = Solution()
  print(test.groupAnagrams(num))
