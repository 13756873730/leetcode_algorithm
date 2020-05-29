class Solution:
    def isIsomorphic(self, s, t) -> bool:
        if not len(s) == len(t):
            return False
        dictionary = {}
        for index in range(len(s)):
            s_letter = s[index]
            t_letter = t[index]
            predict = dictionary.get(s_letter)
            if predict is None:
                dictionary[s_letter] = t_letter
                if not len(set(dictionary.values())) == len(dictionary.keys()):
                    return False
            elif not t_letter.__eq__(predict):
                return False

        return True


if __name__ == '__main__':
    s = "aba"
    t = "baa"

    result = Solution().isIsomorphic(s, t)
    print(result)
    pass
