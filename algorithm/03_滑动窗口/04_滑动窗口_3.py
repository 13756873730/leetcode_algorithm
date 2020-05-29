class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, 1
        max_distance = 1

        while right < len(s):
            for index in range(left, right):
                if s[index].__eq__(s[right]):
                    left = index + 1
                    break
            max_distance = max(right - left + 1, max_distance)
            right += 1
        return max_distance


if __name__ == '__main__':
    s = "pwwkew"
    result = Solution().lengthOfLongestSubstring(s=s)
    print(result)
    pass
