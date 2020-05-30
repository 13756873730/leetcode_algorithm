class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dictionary = {}
        for index, num in enumerate(nums):
            elem = dictionary.get(num)
            if elem is None:
                dictionary[num] = [index]
            else:
                dictionary[num].append(index)

        for key, value in dictionary.items():
            if len(value) < 2:
                continue
            else:
                value = sorted(value)
                for index in range(1, len(value)):
                    if value[index] - value[index - 1] <= k:
                        return True

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    result = Solution().containsNearbyDuplicate(nums, k)
    print(result)
    pass
