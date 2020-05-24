class BiTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return 'BiTree {}'.format(self.value)


if __name__ == '__main__':
    root = BiTree(1)
    root.left = BiTree(11)
    root.right = BiTree(12)
    print(root.right)

    pass
