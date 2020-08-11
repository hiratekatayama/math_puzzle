# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDepth = 0
        def bfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                self.maxDepth = max(self.maxDepth, depth)
            if root.left:
                return bfs(root.left, depth + 1)
            if root.right:
                return bfs(root.right, depth + 1)

        bfs(root, 0)

        return self.maxDepth


if __name__ == "__main_":
    test = Solution()

    node1 = TreeNode(15)
    node2 = TreeNode(7)
    node3 = TreeNode(9)
    node4 = TreeNode(20, node1, node2)
    node5 = TreeNode(3, node3, node4)

    check = test.maxDepth(node5)
    print(check)