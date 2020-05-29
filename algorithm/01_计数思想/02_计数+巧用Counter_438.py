from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        p_len = len(p)
        p_counter = Counter(p)
        index = 0
        result = []
        while index <= len(s) - p_len:
            sub_s = s[index:index + p_len]
            if Counter(sub_s) == p_counter:
                result.append(index)
            index += 1
        return result


if __name__ == '__main__':
    s = 'cbaebabacd'
    p = 'abc'

    result = Solution().findAnagrams(s=s, p=p)
    print(result)
    pass
