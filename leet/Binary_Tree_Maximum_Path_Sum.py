import sys

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        self.res = -sys.maxsize - 1
        self.oneSideSum(root)
        return self.res

    def oneSideSum(self, root):
        if not root:
            return 0
        l = max(0, self.oneSideSum(root.left))
        r = max(0, self.oneSideSum(root.right))
        self.res = max(self.res, l + r + root.val)
        return max(l, r) + root.val

if __name__ == "__main__":
    node5 = TreeNode(7)
    node4 = TreeNode(15)
    node3 = TreeNode(20, node4, node5)
    node2 = TreeNode(9)
    node1 = TreeNode(-10, node2, node3)

    test = Solution()
    print(test.maxPathSum(node1))