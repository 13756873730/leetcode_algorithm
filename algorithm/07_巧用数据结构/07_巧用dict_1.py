class Solution:
    def twoSum(self, nums, target: int):
        result = []
        dictionary = {}
        for index, n in enumerate(nums):
            dict_target = target - n
            dict_result = dictionary.get(dict_target)
            if dict_result is None:
                dictionary[n] = index
            else:
                result = [dict_result, index]
        return result


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    result = Solution().twoSum(nums, target)
    print(result)
    pass
