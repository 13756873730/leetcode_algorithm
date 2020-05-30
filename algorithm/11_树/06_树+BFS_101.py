class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def next_layer(self, node_list):
        children_list = []
        for node in node_list:
            if node is not None:
                children_list.extend([node.left, node.right])
        return children_list

    def get_value(self, node_list):
        value_list = []
        for node in node_list:
            if node is None:
                value_list.append(None)
            else:
                value_list.append(node.val)
        return value_list

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        children_list = self.next_layer([root])
        while len(children_list) > 0:
            value_list = self.get_value(children_list)
            # print(value_list)
            for index in range(int(len(children_list) / 2)):
                if not value_list[index] == value_list[len(children_list) - index - 1]:
                    return False
            children_list = self.next_layer(children_list)
        return True


if __name__ == '__main__':
    # [2,3,3,4,5,5,4, null,null,8,9,null,null,9,8]
    root = TreeNode(2)

    root.left = TreeNode(3)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)

    root.left.left.left = None
    root.left.left.right = None
    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)
    root.right.left.left = None
    root.right.left.right = None
    root.right.right.left = TreeNode(9)
    root.right.right.right = TreeNode(8)
    print(Solution().isSymmetric(root))
