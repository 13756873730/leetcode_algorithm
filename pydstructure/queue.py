class Queue:
    def __init__(self, capacity=128, initial_elements=None):
        self.capacity = capacity
        self.elements = [] if initial_elements is None else initial_elements
        self.count = len(self.elements)

    def __repr__(self):
        return 'Queue({0}/{1}) {2}'.format(self.count, self.capacity, self.elements)

    def is_empty(self):
        return self.count == 0

    def clear(self):
        self.elements = []
        self.count = 0

    # 队尾入队（生产）
    def product(self, element):
        assert self.capacity > len(self.elements), 'Queue Full Error'
        self.elements.append(element)
        self.count += 1
        return self

    # 获取队首元素
    def get(self):
        assert len(self.elements) > 0, 'Queue Empty Error'
        return self.elements[0]

    # 队首出队（消费）
    def consume(self):
        assert len(self.elements) > 0, 'Queue Empty Error'
        self.count -= 1
        return self.elements.pop(0)

    def consume_all(self):
        elements = []
        while self.count > 0:
            elements.append(self.consume())
        return elements

    # B队列consume之后，做为A队列的product
    def __add__(self, another):
        while another.count > 0:
            self.product(another.consume())
        return self


if __name__ == '__main__':
    queue = Queue(capacity=100, initial_elements=[1, '2', True, 'abc', '1.23'])
    print(queue)
    print(queue.is_empty())

    queue.product('XXX')
    print(queue)

    elem = queue.consume()
    print(elem, queue)

    elem = queue.get()
    print(elem, queue)

    queue.clear()
    print(queue)


    a = Queue(initial_elements=[1, 2, 3])
    b = Queue(initial_elements=[4, 5, 6])
    a + b
    print(a, b)
    pass
