class Solution:
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        result = []
        for value in nums1_set:
            if nums2_set.__contains__(value):
                result.append(value)
        return result


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]

    result = Solution().intersection(nums1=nums1, nums2=nums2)
    print(result)
    pass
