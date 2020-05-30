class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count = 1
        count = count + self.countNodes(root.left)
        count = count + self.countNodes(root.right)
        return count
