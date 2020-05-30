class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []

        # 排序
        nums = sorted(nums)
        # 数据处理
        min_num = target - nums[len(nums) - 1] - nums[len(nums) - 2] - nums[len(nums) - 3]
        max_num = target - nums[0] - nums[1] - nums[2]
        while len(nums) > 0 and nums[0] < min_num:
            nums.pop(0)
        while len(nums) > 0 and nums[len(nums) - 1] > max_num:
            nums.pop(len(nums) - 1)
        # 遍历
        result = []
        index_a = 0
        while index_a < len(nums) - 3:
            if index_a > 0 and nums[index_a] == nums[index_a - 1]:
                index_a += 1
                continue
            index_b = index_a + 1
            check_repeat_b = False
            while index_b < len(nums) - 2:
                if check_repeat_b and index_b > 1 and nums[index_b] == nums[index_b - 1]:
                    index_b += 1
                    continue
                check_repeat_b = True
                target2 = target - (nums[index_a] + nums[index_b])
                left, right = index_b + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == target2:
                        result.append([nums[index_a], nums[index_b], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
                    elif nums[left] + nums[right] < target2:
                        while left < right and nums[left] + nums[right] < target2:
                            left += 1
                    else:
                        while left < right and nums[left] + nums[right] > target2:
                            right -= 1
                index_b += 1
            index_a += 1
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    target = -1

    result = Solution().fourSum(nums, target)
    print(result)
    pass
