class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'LinkList {}'.format(self.iterate())

    def iterate(self):
        elements = []
        node = self
        while node is not None:
            elements.append(node.value)
            node = node.next
        return elements


if __name__ == '__main__':
    root = Node(10)
    root.next = Node(False)
    root.next.next = Node(8.12)
    print(root)

    root = root.next
    print(root)
    pass
