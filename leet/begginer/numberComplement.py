class Solution(object):
  def findComplement(self, num):
    bin_num = bin(5)
    bin_num = list(bin_num)
    
    for i in range(2,len(bin_num)):
      if int(bin_num[i]) == 1:
        bin_num[i] = '0'
      else:
        bin_num[i] = '1'
    
    bin_num = ''.join(bin_num)
    return int(bin_num, 2)

  def findComplement_2(self, num):
    i = 1
    while i <= num:
      i = i << 1
      print(i, num)
    return (i-1) ^ num

if __name__ == '__main__':
  num = 5
  test = Solution()
  print(test.findComplement(num))
  print(test.findComplement_2(num))
