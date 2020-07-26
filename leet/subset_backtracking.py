import queue

class Solution(object):
  def permutation(self, nums):
    output = [[]]
    
    for i in nums:
      output += [curr + [i] for curr in output]

    return output

  def subset(self, nums):
    def backtracking(first = 0, curr = []):
      if len(curr) == k:
        output.append(curr[:])
        #print("output",output, "k", k)
      for i in range(first, n):
        #print(first, n, curr)
        curr.append(nums[i])
        #print(i, curr)
        #print()
        backtracking(i+1, curr)
        #print("test")
        curr.pop()

    output = []
    n = len(nums)
    for k in range(n+1):
      backtracking()
    return output

  def BFS_track(self, nums):
    curr = []
    #if len(curr) == 3:
    #  output.append(curr[:])
    #  return output

    q = queue.Queue()
    for i in nums:
      q.put(i)

    while not q.empty():
      test = q.get()
      curr.append(test)
      print(curr)


  def bitmask(self, nums):
    nth_bit = 1 << n;
    for i in range(2**n):
      bitmask = bin(i | nth_bit)[3:]

if __name__ == '__main__':
  test = Solution()

  nums = [1,2,3]

  #print(test.permutation(nums))

  #print(test.subset(nums))
  #print(test.bitmask(nums))
  print(test.BFS_track(nums))
