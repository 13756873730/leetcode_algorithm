class Solution:
    def reverseVowels(self, s: str):
        letters = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        s_list = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not letters.__contains__(s[left]):
                left += 1
            while left < right and not letters.__contains__(s[right]):
                right -= 1
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        s = ''.join(s_list)
        return s


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    s = "leetcode"

    result = Solution().reverseVowels(s=s)
    print(result)
    pass
