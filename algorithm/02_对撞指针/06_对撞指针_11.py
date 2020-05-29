class Solution:
    @staticmethod
    def get_area(height, left, right):
        return (right - left) * min(height[left], height[right])

    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        max_area = self.get_area(height, left, right)

        while left < right:
            if height[left] >= height[right]:
                # 左高，右侧左移
                src_left, src_right = left, right
                while left < right and height[right] <= height[src_right]:
                    right -= 1
            else:
                # 右高，左侧右移
                src_left, src_right = left, right
                while left < right and height[left] <= height[src_left]:
                    left += 1
            if left < right:
                area = self.get_area(height, left, right)
                if max_area < area:
                    max_area = area
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = Solution().maxArea(height=height)
    print(result)
    pass
