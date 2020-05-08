class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution(object):
  def middleNode(self, head):
    A = [head]
    while A[-1].next:
      A.append(A[-1].next)
    return A[len(A)/2]

if __name__ == '__main__':
  num = [1,2,3,4,5]
  li_node = LinstNode()
  test    = Solution()
  print(test.middleNode(num))
