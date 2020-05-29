from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        s_list = []
        for key, count in s_counter.most_common():
            s_list.extend([key for _ in range(count)])
        return ''.join(s_list)


if __name__ == '__main__':
    s = "tree"

    result = Solution().frequencySort(s)
    print(result)
    pass
