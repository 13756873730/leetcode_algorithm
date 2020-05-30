class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        # 排序
        nums = sorted(nums)
        # 数据处理
        min_num = 0 - nums[len(nums) - 1] - nums[len(nums) - 2]
        max_num = 0 - nums[0] - nums[1]
        while len(nums) > 0 and nums[0] < min_num:
            nums.pop(0)
        while len(nums) > 0 and nums[len(nums) - 1] > max_num:
            nums.pop(len(nums) - 1)
        # 遍历
        result = []
        index = 0
        while index < len(nums) - 2:
            if index > 0 and nums[index] == nums[index - 1]:
                index += 1
                continue
            target = 0 - nums[index]
            left, right = index + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    while left < right and nums[left] + nums[right] < target:
                        left += 1
                else:
                    while left < right and nums[left] + nums[right] > target:
                        right -= 1
            index += 1
        return result


if __name__ == '__main__':
    nums = [-4, -2, -1]

    result = Solution().threeSum(nums)
    print(result)
    pass
