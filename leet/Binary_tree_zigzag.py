from collections import deque

class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def zigzagLevelOrder(self, root):
    if not root:
      return []
    queue = deque([root])
    result, direction = [], 1

    while queue:
      level = []
      for i in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      result.append(level[::direction])
      direction *= (-1)
    return result

if __name__ == '__main__':
  test = Solution()

  node = TreeNode()
  node.val = 3
  node.left = TreeNode()
  node.left.val = 9
  node.left.left = TreeNode()
  node.left.right = TreeNode()

  node.right = TreeNode()
  node.right.val = 20
  node.right.left = TreeNode()
  node.right.left.val = 15
  node.right.right = TreeNode()
  node.right.right.val = 7

  print(test.zigzagLevelOrder(node))
  
