class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if len(nums) == 0:
            return 0

        min_distance = len(nums) + 1
        left, right = 0, 1
        count = nums[left]
        if count >= s:
            return 1

        while right < len(nums):
            count += nums[right]
            while count >= s:
                min_distance = min(right - left + 1, min_distance)
                count -= nums[left]
                left += 1
            right += 1
        return 0 if min_distance == len(nums) + 1 else min_distance


if __name__ == '__main__':
    s = 90
    nums = [2, 3, 1, 2, 4, 3]

    result = Solution().minSubArrayLen(s=s, nums=nums)
    print(result)
    pass
