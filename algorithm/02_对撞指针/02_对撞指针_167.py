class Solution:
    def twoSum(self, numbers, target: int):
        left, right = 0, len(numbers) - 1
        index1, index2 = left, right
        while left < right:
            # cur < target: left += 1
            while left < right and numbers[left] + numbers[right] < target:
                left += 1
            # cur > target: right -= 1
            while left < right and numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] == target:
                index1, index2 = left, right
                break
        return [index1 + 1, index2 + 1]


if __name__ == '__main__':
    # array = generator.random_array()
    numbers = [2, 7, 11, 15]
    target = 9

    result = Solution().twoSum(numbers=numbers, target=target)
    print(result)
    pass
