from utils.generator import Generator


class Solution:
    def moveZeroes(self, nums) -> None:
        # 统计0的个数zero_count，非0个数为len(nums) - zero_count
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1

        # 填充非零位置
        left_index = 0
        right_index = 0
        while right_index < len(nums):
            if nums[right_index] != 0:
                nums[left_index] = nums[right_index]
                left_index += 1
            right_index += 1

        # 填充零元素
        while left_index < len(nums):
            nums[left_index] = 0
            left_index += 1

        return


if __name__ == '__main__':
    generator = Generator(
        size=5,
        low=0,
        high=10,
    )
    # array = generator.random_array()
    array = [0, 1, 0, 3, 12]

    Solution().moveZeroes(nums=array)
    print(array)
    pass
