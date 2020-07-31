class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        def flat(root):
            print(root.val)
            if not root:
                return
            flat(root.right)
            flat(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
        self.prev = None
        flat(root)

        return root

if __name__ == "__main__":
    test = Solution()

    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node2 = TreeNode(2, node3, node4)
    node5 = TreeNode(5, TreeNode,node6)
    node  = TreeNode(1, node2, node5)
    print(test.flatten(node))
