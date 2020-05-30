class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        result = 0
        dict1 = {}
        dict2 = {}
        for a in A:
            for b in B:
                count = a + b
                elem = dict1.get(count)
                if elem is None:
                    dict1[count] = 1
                else:
                    dict1[count] = elem + 1
        for c in C:
            for d in D:
                count = c + d
                elem = dict2.get(count)
                if elem is None:
                    dict2[count] = 1
                else:
                    dict2[count] = elem + 1
        for key, value in dict1.items():
            elem = dict2.get((0 - key))
            if elem is not None:
                result = result + value * elem
        return result


if __name__ == '__main__':
    """
    0 0 1 0|0 1 0 0|0 1 1 1|1 0 1 0|1 1 0 0|1 0 1 0
    -2   2 | 0   0 | 0   0 | -2  2 | 0   0 | 0   0|
    """
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]

    result = Solution().fourSumCount(A, B, C, D)
    print(result)
    pass
