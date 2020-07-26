import bisect

class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def bstFromPreorder(self, preorder): #O(N^2)
    if not preorder:
      return None
    root = TreeNode(preorder[0])
    i = bisect.bisect(preorder, preorder[0])
    root.left = self.bstFromPreorder(preorder[1:i])
    root.right = self.bstFromPreorder(preorder[i:])
    return root

  def bstFromPreorder_2(self, A):
    def helper(i, j):
      if i == j:
        return None
      root = TreeNode(A[i])
      mid = bisect.bisect(A, A[i], i+1, j)
      root.left = helper(i+1, mid)
      root.right = helper(mid, j)
      return root
    return helper(0, len(A))

if __name__ == '__main__':
  input = [8,5,1,7,10,12]
  test = Solution()
  
  result = test.bstFromPreorder_2(input)

  #print(result.val)
