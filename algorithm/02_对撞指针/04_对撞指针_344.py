class Solution:
    def reverseString(self, s) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    s = ["H","a","n","n","a","h"]

    Solution().reverseString(s=s)
    print(s)
    pass
