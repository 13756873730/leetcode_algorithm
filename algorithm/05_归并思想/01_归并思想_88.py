class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        cur_index = m + n - 1
        while (index1 >= 0) and (index2 >= 0):
            if nums1[index1] >= nums2[index2]:
                nums1[cur_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[cur_index] = nums2[index2]
                index2 -= 1
            cur_index -= 1
        while index2 >= 0:
            nums1[cur_index] = nums2[index2]
            index2 -= 1
            cur_index -= 1
        return

if __name__ == '__main__':
    array1 = [1, 2, 3, 0, 0, 0]
    m = 3
    array2 = [2, 5, 6]
    n = 3

    Solution().merge(nums1=array1, m=m, nums2=array2, n=n)
    print(array1)  # [1,2,2,3,5,6]
    pass
