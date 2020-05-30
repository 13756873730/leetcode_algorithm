class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_deep(self, root):
        if root is None:
            return 0
        return max(self.get_deep(root.left), self.get_deep(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if abs(self.get_deep(root.left) - self.get_deep(root.right)) >= 2:
            return False
        if root.left is not None:
            if not self.isBalanced(root.left):
                return False
        if root.right is not None:
            if not self.isBalanced(root.right):
                return False
        return True


if __name__ == '__main__':
    # [3, 9,20, null,null,15,7]
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(3)

    print(Solution().isBalanced(root))
