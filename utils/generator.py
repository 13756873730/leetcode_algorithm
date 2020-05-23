import random


class Generator:

    def __init__(self, size=10, low=-99, high=100, dtype='int',
                 decimal_format='%.2f', sort=None, seed=None):
        self.size = size
        self.low = low
        self.high = high
        self.dtype = dtype
        self.decimal_format = decimal_format
        self.sort = sort
        self.seed = seed

    def random_array(self):
        # 随机种子
        if self.seed is not None:
            random.seed(self.seed)

        # 封装数据
        if self.dtype == 'int':
            array = [
                random.randint(self.low, self.high)
                for _ in range(self.size)
            ]
        elif self.dtype == 'float':
            array = [
                self.decimal_format % (random.random() * (self.high - self.low) + self.low)
                for _ in range(self.size)
            ]
        else:
            raise Exception(' ### Parameters Error: <dtype> ### ')

        # 排序规则
        if self.sort is not None:
            if str(self.sort).__eq__('asc'):
                array.sort()
            elif str(self.sort).__eq__('desc'):
                array.sort(reverse=True)
            else:
                raise Exception(' ### Parameters Error: <sort> ### ')

        return array


if __name__ == '__main__':
    generator = Generator(size=5, low=0, high=10, sort='desc', dtype='float', decimal_format='%.3f')
    array = generator.random_array()
    print(array)
    pass
