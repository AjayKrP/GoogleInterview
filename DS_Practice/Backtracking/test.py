import math
import random


class Solution:
    def generate(self, A, temp, result, freq):
        flag = 0
        if len(temp) == len(A):
            result.append(temp[:])
            return
        else:
            for key, val in freq.items():
                if val > 0:
                    freq[key] -= 1
                    temp.append(key)
                    if len(temp) > 1:
                        if math.ceil(math.sqrt(temp[-1] + temp[-2])) == math.floor(math.sqrt(temp[-1] + temp[-2])):
                            self.generate(A, temp, result, freq)
                    else:
                        self.generate(A, temp, result, freq)
                    temp.pop()
                    freq[key] += 1

    def solve(self, A):
        if len(A) == 1:
            return 0
        freq = {}
        for ele in A:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1

        result = []
        visited = len(A) * [0]
        self.generate(A, [], result, freq)
        return len(result)


sol = Solution()
print(sol.solve([1, 17, 8]))


def fun1_6():
    return random.randint(1, 6)


def func_12():
    x = 2 * fun1_6()
    y = fun1_6()
    if y % 2 == 0:
        return x
    else:
        return x - 1
