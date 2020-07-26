import itertools
#cannot understand clearly
class Solution(object):
  def backspaceCompare(self, S, T): #buildString
    a

  def backspaceCompare_2(self, S, T): #twopointer
    def F(S):
      skip = 0
      for x in reversed(S):
        if x == "#":
          skip += 1
        elif skip:
          skip -= 1
        else:
          yield x
    return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))

if __name__ == '__main__':
  input_S = "ab#c"
  input_T = "ad#c"

  test = Solution()
  print(test.backspaceCompare_2(input_S, input_T))
