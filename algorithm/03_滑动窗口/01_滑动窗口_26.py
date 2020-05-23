from utils.generator import Generator


class Solution:
    def removeDuplicates(self, nums) -> int:
        left_index = 0
        right_index = 1

        while right_index < len(nums):
            if nums[left_index] != nums[right_index]:
                left_index += 1
                nums[left_index] = nums[right_index]
            right_index += 1
        return left_index + 1


if __name__ == '__main__':
    generator = Generator(
        size=5,
        low=0,
        high=10,
    )
    # array = generator.random_array()
    array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    result = Solution().removeDuplicates(nums=array)
    print(array, result)
    pass
