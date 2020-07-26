class Solution:
  def isHappy(self, num):
    set_num = set()
    while num != 1:
      a = []
      a = [int(i)**2 for i in str(num)]
      num = sum(a)

      if num in set_num:
        return False
      else:
        set_num.add(num)

    else:
      return True

if __name__ == '__main__':
  input = 19

  test = Solution()
  print(test.isHappy(input))
