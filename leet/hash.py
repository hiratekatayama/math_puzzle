class Solution:
  def singleNumber(self, num):
    count_by_kw = {}

    for i in num:
      if count_by_kw.get(i):
        count_by_kw[i] += 1
      else:
        count_by_kw[i] = 1
      
    for i in count_by_kw:
      if count_by_kw[i] == 1:
        return i

if __name__ == '__main__':
  input = [4,1,2,1,2]

  test = Solution()
  print(test.singleNumber(input))
