class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].islower() and not s[left].isdigit():
                left += 1
            while left < right and not s[right].islower() and not s[right].isdigit():
                right -= 1
            if not s[left].__eq__(s[right]):
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9

    result = Solution().isPalindrome(s='A man, a plan, a canal: Panama')
    print(result)
    pass
