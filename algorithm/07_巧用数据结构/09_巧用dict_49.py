class Solution:
    def groupAnagrams(self, strs):
        dictionary = {}
        for s in strs:
            s_sort = ''.join(sorted(list(s)))
            value = dictionary.get(s_sort)
            if value is None:
                dictionary[s_sort] = [s]
            else:
                dictionary[s_sort].append(s)
        return list(dictionary.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)
    pass
