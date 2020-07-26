# hash
# bit

class Solution:
  def singleNumber(self, num): #simple
    check = num[0]
    i = 1

    while i < len(num):
      if i+1 == len(num):
        return check

      if check == num[i]:
        check = num[i+1]
        i += 1

      i += 1

  def singleNumber_hash(self, num):
    count_by_kw = {}

    for i in num:
      if count_by_kw.get(i):
        count_by_kw[i] += 1
      else:
        count_by_kw[i] = 1

    for i in count_by_kw:
      if count_by_kw[i] == 1:
        return i

  def singleNumber_bit(self, num):
    a = 0
    for i in num:
      a ^= i
    return a

if __name__ == '__main__':
  input = [4,1,2,1,2]

  test = Solution()
  print(test.singleNumber(input))
  print(test.singleNumber_hash(input))
  print(test.singleNumber_bit(input))
