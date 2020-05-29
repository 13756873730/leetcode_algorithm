from collections import Counter


class Solution:
    @staticmethod
    def contains(sub_s, t_counter):
        s_counter = Counter(sub_s)
        if len(s_counter.keys()) < len(t_counter.keys()):
            return False
        for key, count in t_counter.items():
            if s_counter.get(key) is None or s_counter.get(key) < count:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        left = 0
        right = 1
        min_distance = len(s) + 1
        result = ''
        while right <= len(s):
            while right < len(s) and not self.contains(s[left:right], t_counter):
                right += 1
            while self.contains(s[left:right], t_counter):
                if right - left < min_distance:
                    min_distance = right - left
                    result = s[left:right]
                    if min_distance == len(t):
                        return result
                left += 1
            right += 1
        return result


if __name__ == '__main__':
    s = 'CBANC'
    t = 'ANC'

    result = Solution().minWindow(s=s, t=t)
    print(result)
    pass
