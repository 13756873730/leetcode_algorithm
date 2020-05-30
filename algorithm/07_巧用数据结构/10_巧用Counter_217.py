from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == 0:
            return False
        return list(Counter(nums).most_common(1))[0][1] > 1


if __name__ == '__main__':
    nums = [2, 14, 18, 22, 22]
    result = Solution().containsDuplicate(nums)
    print(result)
    pass
