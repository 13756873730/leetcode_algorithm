class Solution:
    def isHappy(self, n: int):
        def get_square_sum(number):
            number_list = []
            while number > 0:
                t = number % 10
                number_list.append(t)
                number = int(number / 10)
            return sum([x ** 2 for x in number_list])

        if n == 1:
            return True

        number_list = []
        while n != 1:
            n = get_square_sum(n)
            if n == 1:
                return True
            if number_list.__contains__(n):
                return False
            else:
                number_list.append(n)


if __name__ == '__main__':
    n = 2

    result = Solution().isHappy(n)
    print(result)
    pass
