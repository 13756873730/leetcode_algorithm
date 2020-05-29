from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)
        result = []
        for key, count1 in nums1_counter.items():
            if nums2_counter.__contains__(key):
                count2 = nums2_counter.get(key)
                result.extend([key for _ in range(min(count1, count2))])
        return result


if __name__ == '__main__':
    nums1 = [4, 4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]

    result = Solution().intersect(nums1=nums1, nums2=nums2)
    print(result)
    pass
