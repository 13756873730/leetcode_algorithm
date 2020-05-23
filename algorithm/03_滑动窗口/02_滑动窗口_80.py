from utils.generator import Generator


class Solution:
    def removeDuplicates(self, nums) -> int:
        left_index = 0
        right_index = 0

        while right_index < len(nums):
            count = 1
            index = right_index + 1
            while (index < len(nums)) and (nums[index] == nums[right_index]):
                count += 1
                index += 1
            count = min(count, 2)
            for i in range(count):
                nums[left_index] = nums[right_index]
                left_index += 1
            right_index = index

        return left_index


if __name__ == '__main__':
    generator = Generator(
        size=5,
        low=0,
        high=10,
    )
    # array = generator.random_array()
    array = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    result = Solution().removeDuplicates(nums=array)
    print(array, result)
    pass
