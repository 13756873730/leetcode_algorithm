from utils.generator import Generator


class Solution:
    def removeElement(self, nums, val: int) -> int:
        left_index = 0
        right_index = len(nums)

        while left_index < right_index:
            if nums[left_index] == val:
                right_index -= 1
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
                left_index -= 1
            left_index += 1
        return left_index


if __name__ == '__main__':
    generator = Generator(
        size=5,
        low=0,
        high=10,
    )
    # array = generator.random_array()
    array = [0, 1, 2, 2, 3, 0, 4, 2]

    result = Solution().removeElement(nums=array, val=2)
    print(array, result)
    pass
