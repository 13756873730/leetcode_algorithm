class Solution:
    def quick_sort(self, array, start, end, target):
        if start >= end:
            return array
        left, right = start, end
        pivot = left
        while left < right:
            # right左移
            while left < right and array[left] <= array[right]:
                right -= 1
            array[left], array[right] = array[right], array[left]
            pivot = right
            # left 右移
            while left < right and array[left] <= array[right]:
                left += 1
            array[left], array[right] = array[right], array[left]
            pivot = left
        if target == pivot:
            return array
        elif target < pivot:
            array = self.quick_sort(array, start=start, end=pivot - 1, target=target)
        else:
            array = self.quick_sort(array, start=pivot + 1, end=end, target=target)
        return array

    def findKthLargest(self, nums, k: int) -> int:
        array = self.quick_sort(array=nums, start=0, end=len(nums) - 1, target=len(nums) - k)
        return array[len(nums) - k]


if __name__ == '__main__':
    array = [3, 2, 1, 5, 6, 4]
    k = 2

    result = Solution().findKthLargest(nums=array, k=k)
    print(result)
    pass
