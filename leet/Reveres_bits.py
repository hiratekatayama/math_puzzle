class Solution(object):
  def bit_by_bit(self, n):
    ret, power = 0, 31
    while n:
      ret += (n&1) << power
      n = n >> 1
      power -= 1
    return ret

  def byte_by_byte(self,n):
    ret, power = 0, 24
    cache = dict()
    while n:
      ret += self.reverseByte(n & 0xff, cache) << power
      n = n >> 8
      power -= 8
    return ret

  def reverseByte(self, byte, cache):
    if byte not in cache:
      cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
    return cache[byte]

  def mask_and_shift():
    pass

if __name__ == '__main__':
  test = Solution()
  check = 13
  print(test.bit_by_bit(check))
  print(test.byte_by_byte(check))
