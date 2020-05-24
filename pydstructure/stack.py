class Stack:
    def __init__(self, capacity=128, initial_elements=None):
        self.capacity = capacity
        self.elements = [] if initial_elements is None else initial_elements
        self.count = len(self.elements)

    def __repr__(self):
        return 'Stack({0}/{1}) {2}'.format(self.count, self.capacity, self.elements)

    def is_empty(self):
        return self.count == 0

    def clear(self):
        self.elements = []
        self.count = 0

    # 入栈
    def push(self, element):
        assert self.capacity > len(self.elements), 'Stack Full Error'
        self.elements.append(element)
        self.count += 1
        return self

    # 获取栈顶元素
    def get(self):
        assert len(self.elements) > 0, 'Stack Empty Error'
        return self.elements[len(self.elements) - 1]

    # 出栈
    def pop(self):
        assert len(self.elements) > 0, 'Stack Empty Error'
        self.count -= 1
        return self.elements.pop(len(self.elements) - 1)

    def pop_all(self):
        elements = []
        while self.count > 0:
            elements.append(self.pop())
        return elements

    # B栈pop之后，push到A栈
    def __add__(self, another):
        while another.count > 0:
            self.push(another.pop())
        return self


if __name__ == '__main__':
    stack = Stack(capacity=5)
    print(stack.is_empty())

    stack.push(1).push(2).push(3).push(1.23).push('abc')
    print(stack)
    print(stack.is_empty())

    print(stack.get())

    elem = stack.pop()
    print(elem)
    print(stack)

    elem = stack.pop()
    print(elem)
    print(stack)

    stack.clear()
    print(stack)

    a = Stack().push(1).push(2).push(3)
    b = Stack().push(4).push(5).push(6)
    c = a + b
    print(c, a.count, b.count)

    elements = c.pop_all()
    print(elements)
    print(c.is_empty())
    pass
