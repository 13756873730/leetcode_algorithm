class Solution:
    def wordPattern(self, pattern, str):
        pattern_list = list(pattern)
        str_list = str.split(' ')
        if not len(pattern_list) == len(str_list):
            return False
        dictionary = {}
        for index in range(len(pattern_list)):
            pattern_letter = pattern[index]
            str_word = str_list[index]
            predict = dictionary.get(pattern_letter)
            if predict is None:
                dictionary[pattern_letter] = str_word
                if not len(set(dictionary.values())) == len(dictionary.keys()):
                    return False
            elif not predict.__eq__(str_word):
                return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    str = "dog dog dog dog"

    result = Solution().wordPattern(pattern, str)
    print(result)
    pass
