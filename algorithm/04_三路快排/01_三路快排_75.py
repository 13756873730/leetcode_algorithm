class Solution:
    def sortColors(self, nums) -> None:
        left_index = -1
        right_index = len(nums)
        cur_index = 0

        while cur_index < right_index:
            if nums[cur_index] == 0:
                left_index += 1
                nums[left_index], nums[cur_index] = nums[cur_index], nums[left_index]
                cur_index += 1
            elif nums[cur_index] == 1:
                cur_index += 1
            else:
                right_index -= 1
                nums[cur_index], nums[right_index] = nums[right_index], nums[cur_index]


if __name__ == '__main__':
    array = [2, 0, 2, 1, 1, 0]

    Solution().sortColors(nums=array)
    print(array)
    pass
