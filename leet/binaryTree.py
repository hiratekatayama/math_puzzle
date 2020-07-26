class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def diameterOfBinaryTree(self, root): #depthFirstSearch
    self.ans = 1
    def depth(node):
      if not node: return 0
      L = depth(node.left)
      R = depth(node.right)
      self.ans = max(self.ans, L+R+1)
      return max(L,R) + 1

    depth(root)
    return self.ans - 1

if __name__ == '__main__':
  a
