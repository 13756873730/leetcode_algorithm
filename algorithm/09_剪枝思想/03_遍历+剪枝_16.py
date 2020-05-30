class Solution:
    def threeSumClosest(self, nums, target):
        # 排序
        nums = sorted(nums)
        # 遍历
        min_distance = abs(sum(nums[:3]) - target)
        result = sum(nums[:3])
        index = 0
        while index < len(nums) - 2:
            if index > 0 and nums[index] == nums[index - 1]:
                index += 1
                continue
            target2 = target - nums[index]
            left, right = index + 1, len(nums) - 1
            while left < right:
                distance = abs(nums[left] + nums[right] - target2)
                if distance < min_distance:
                    min_distance = distance
                    result = nums[index] + nums[left] + nums[right]
                if nums[left] + nums[right] == target2:
                    return target
                elif nums[left] + nums[right] < target2:
                    left += 1
                else:
                    right -= 1
            index += 1
        return result


if __name__ == '__main__':
    nums = [0, 2, 1, -3]
    target = 1

    result = Solution().threeSumClosest(nums, target)
    print(result)
    pass
