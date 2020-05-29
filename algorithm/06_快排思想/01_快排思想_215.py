class Solution:
    def quick_sort(self, nums, start, end, target):
        if start >= end:
            return nums
        left, right = start, end
        pivot = left
        while left < right:
            # right左移
            while left < right and nums[pivot] <= nums[right]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            pivot = right
            while left < right and nums[left] <= nums[pivot]:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
            pivot = left
        if target == pivot:
            return nums
        elif target < pivot:
            return self.quick_sort(nums=nums, start=start, end=pivot - 1, target=target)
        else:
            return self.quick_sort(nums=nums, start=pivot + 1, end=end, target=target)

    def findKthLargest(self, nums, k: int) -> int:
        nums = self.quick_sort(nums=nums, start=0, end=len(nums) - 1, target=len(nums) - k)
        return nums[len(nums) - k]


if __name__ == '__main__':
    array = [3, 2, 1, 5, 6, 4]
    k = 2

    result = Solution().findKthLargest(nums=array, k=k)
    print(result)
    pass
