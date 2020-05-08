class Solution(object):
  def sortedSquares(self, A):
    num_list = [i**2 for i in A]
    num_list = sorted(num_list)

    return num_list

  def sortedSquares_2(self, A): #twoPointer
    N = len(A)
    j = 0
    while j < N and A[j] < 0:
      j += 1
    i = j - 1

    ans = []
    while 0 <= i and j < N:
      if A[i]**2 < A[j]**2:
        ans.append(A[i]**2)
        i -= 1
      else:
        print(i, j)
        ans.append(A[j]**2)
        j += 1

    while i >= 0:
      ans.append(A[i]**2)
      i -= 1
    while j < N:
      print(i, j)
      print(ans)
      ans.append(A[j]**2)
      j += 1
    return ans


if __name__ == '__main__':
  input = [-4, -1, 0, 3, 10]

  test = Solution()
  print(test.sortedSquares_2(input))
